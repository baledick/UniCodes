#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

int main()
{
	FILE *fp1, *fp2, *fp3, *fp4;
	double r;
	char *str;
	str = (char*) malloc(sizeof(char)* 100);
	srand(time(0));

	fp1 = fopen("1.test", "w");
	fprintf(fp1, "ko");
	fclose(fp1);

	r = sin(rand());

	fp2 = fopen("2.test", "w");
	fprintf(fp2, "%lf", r);
	fclose(fp2);

	fp3 = fopen("1.test", "r");
	fscanf(fp3, "%s", str);
	printf("%s\n", str);
	fp4 = fopen("2.test", "r");
	fscanf(fp4, "%s", str);
	printf("%s\n", str);
	fclose(fp3);
	fclose(fp4);
	return 0;
}
