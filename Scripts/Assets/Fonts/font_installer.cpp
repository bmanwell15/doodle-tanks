#include <windows.h>
#include <shlwapi.h> // For PathFileExists
#include <tchar.h> // For _T macro
#include <cstdio>

#pragma comment(lib, "shlwapi.lib")

bool IsFontInstalled(const TCHAR* fontName) {
    HKEY hKey;
    TCHAR regPath[MAX_PATH];
    wsprintf(regPath, _T("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts"));
    
    if (RegOpenKeyEx(HKEY_LOCAL_MACHINE, regPath, 0, KEY_QUERY_VALUE, &hKey) == ERROR_SUCCESS) {
        TCHAR buffer[MAX_PATH];
        DWORD bufferSize = sizeof(buffer);
        LONG result = RegQueryValueEx(hKey, fontName, NULL, NULL, (LPBYTE)buffer, &bufferSize);
        RegCloseKey(hKey);
        return (result == ERROR_SUCCESS);
    }
    return false;
}

bool InstallFont(const TCHAR* fontPath) {
    // Check if the font file exists
    if (!PathFileExists(fontPath)) {
        printf(("Font file does not exist: %s\n"), fontPath);
        return false;
    }

    printf("Path does exist!\n");

    // Copy font file to Windows Fonts directory
    TCHAR fontsDir[MAX_PATH];
    GetWindowsDirectory(fontsDir, MAX_PATH);
    PathAppend(fontsDir, _T("Fonts"));

    
    TCHAR fontFileName[MAX_PATH];
    _tsplitpath_s(fontPath, NULL, 0, NULL, 0, fontFileName, MAX_PATH, NULL, 0);

    
    TCHAR destinationPath[MAX_PATH];
    PathCombine(destinationPath, fontsDir, fontFileName);
    
    if (CopyFile(fontPath, destinationPath, FALSE) == 0) {
        printf(("Failed to copy font file. Error code: %d\n"), GetLastError());
        return false;
    }

    printf("Coppied file...\n");

    // Install the font using AddFontResource
    if (AddFontResource(destinationPath) == 0) {
        printf(("Failed to add font resource. Error code: %d\n"), GetLastError());
        return false;
    }

    printf("Added font...\n");

    // Notify the system of the new font
    HWND hwnd = GetDesktopWindow(); // Get a handle to the desktop window
    if (PostMessage(hwnd, WM_FONTCHANGE, 0, 0) == 0) {
        printf(("Failed to post font change message. Error code: %d\n"), GetLastError());
        return false;
    }
    return true;
}

int _tmain(int argc, _TCHAR* argv[]) {
    if (argc != 2) {
        printf(("Usage: %s <font_path>\n"), argv[0]);
        return 1;
    }

    TCHAR* fontPath = argv[1];

    // Derive font name from the file name
    TCHAR fontFileName[MAX_PATH];
    _tsplitpath_s(fontPath, NULL, 0, NULL, 0, fontFileName, MAX_PATH, NULL, 0);

    printf("Validating file...\n");
    // Check if the font is already installed
    if (IsFontInstalled(fontFileName)) {
        printf(("Font '%s' is already installed.\n"), fontFileName);
        return 0;
    }

    printf("File validated. Adding font...\n");

    // Install the font
    if (InstallFont(fontPath)) {
        printf(("Font installed successfully.\n"));
    } else {
        printf(("Failed to install font.\n"));
    }

    return 0;
}
