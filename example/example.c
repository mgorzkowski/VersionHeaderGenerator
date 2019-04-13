#include <stdio.h>
#include "../version.h"


void printInfos(void)
{
	printf("NAME\t\t= %s\n", NAME);
	printf("VERSION\t\t= %d.%d.%d\n", MAJOR, MINOR, PATCH);
	printf("DESC\t\t= %s\n", DESCRIPTION);
	printf("GITBRANCH\t= %s\n", GIT_BRANCH);
	printf("GITREV\t\t= %s\n", GIT_REVISION_HASH);
	printf("GITSREV\t\t= %s\n", GIT_SHORT_REVISION_HASH);
	printf("MAJOR\t\t= %d\n", MAJOR);
	printf("MINOR\t\t= %d\n", MINOR);
	printf("PATCH\t\t= %d\n", PATCH);
}

int main(void)
{
	printInfos();
	return 0;
}