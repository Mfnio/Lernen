#include <stdio.h>

enum Company {GOOGLE, FACEBOOK, XEROX, YAHOO, EBAY, MICROSOFT};

int main()
{
    enum Company Facebook = FACEBOOK;
    enum Company Google = GOOGLE;
    enum Company Xerox = XEROX;
    printf("Facebook is %d\nGoogle is %d\nXerox is %d\n", Facebook, Google, Xerox);
    return 0;
}