#include <stdio.h>

int main() {
    printf("Hello, this is a test binary with embedded signature.\n");
    // Embedded signature in .eng section simulation via string
    const char* sig = "ENG_BARKI_MUSTAPHA_EMBEDDED_2027_MOROCCO";
    printf("Signature: %s\n", sig);
    return 0;
}
