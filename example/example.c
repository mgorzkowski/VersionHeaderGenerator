#include <stdio.h>
#include "../version.h"


void printInfos(void)
{
	printf("NAME\t\t=\t%s\n", NAME);
	printf("VERSION\t\t=\t%d.%d.%d\n", MAJOR, MINOR, PATCH);
	printf("DESCRIPTION\t=\t%s\n", DESCRIPTION);
	printf("GITBRANCH\t=\t%s\n", GIT_BRANCH);
	printf("GITREV\t\t=\t%s\n", GIT_REVISION_HASH);
	printf("GITSREV\t\t=\t%s\n", GIT_SHORT_REVISION_HASH);
	printf("MAJOR\t\t=\t%d\n", MAJOR);
	printf("MINOR\t\t=\t%d\n", MINOR);
	printf("PATCH\t\t=\t%d\n", PATCH);
	printf("GENTIME\t\t=\t%s\n", GENERATION_TIME);
	printf("GENDATE\t\t=\t%s\n", GENERATION_DATE);
}

int main(void)
{
	printInfos();
	return 0;
}