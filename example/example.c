#include <stdio.h>
#include "../version.h"


void printInfos(void)
{
	printf("DEFINE NAME\t|\tVALUE\n");
	printf("==================================================================================\n");
	printf("NAME\t\t|\t%s\n", NAME);
	printf("VERSION\t\t|\t%d.%d.%d\n", MAJOR, MINOR, PATCH);
	printf("DESCRIPTION\t|\t%s\n", DESCRIPTION);
	printf("==================================================================================\n");
	printf("GITBRANCH\t|\t%s\n", GIT_BRANCH);
	printf("GITREV\t\t|\t%s\n", GIT_REVISION_HASH);
	printf("GITSREV\t\t|\t%s\n", GIT_SHORT_REVISION_HASH);
	printf("==================================================================================\n");
	printf("MAJOR\t\t|\t%d\n", MAJOR);
	printf("MINOR\t\t|\t%d\n", MINOR);
	printf("PATCH\t\t|\t%d\n", PATCH);
	printf("==================================================================================\n");
	printf("GENTIME\t\t|\t%s\n", GENERATION_TIME);
	printf("GENDATE\t\t|\t%s\n", GENERATION_DATE);
	printf("COMPTIME\t|\t%s\n", COMPILATION_TIME);
	printf("COMPDATE\t|\t%s\n", COMPILATION_DATE);
	printf("==================================================================================\n");

}

int main(void)
{
	printInfos();
	return 0;
}