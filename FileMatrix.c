#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main(){
	FILE *fp;
	int n, i, j;
	printf("Dwse n ");
	scanf("%d", &n);
	
	int a[n][n], b[n][n];
	fp = fopen("kopa.kabana", "w");
	for(i=0; i<n; i++){
		for(j=0; j<n; j++){
			printf("Dwse tin timi tou pinaka a stin thesi [%d][%d]", i,j);
			scanf("%d", &a[i][j]);
			fprintf(fp, "%d ", a[i][j]);
		}
		fprintf(fp, "\n");
	}

	for(i=0; i<n; i++){
		fprintf(fp, "\t");
		for(j=0; j<n; j++){
			printf("Dwse tin timi tou pinaka b stin thesi [%d][%d]", i,j);
			scanf("%d", &b[i][j]);
			fprintf(fp, " %d", b[i][j]);
		}
		fprintf(fp, "\n");
	}
	return 0;
}
