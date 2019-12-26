#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main(){
	FILE *fp;
	int n, i, j;
	printf("Give the dimensions n ");
	scanf("%d", &n);
	
	int a[n][n], b[n][n];
	fp = fopen("kopa.kabana", "w");
	for(i=0; i<n; i++){
		for(j=0; j<n; j++){
			printf("Give the value of matrix a in [%d][%d]", i,j);
			scanf("%d", &a[i][j]);
			fprintf(fp, "%d ", a[i][j]);
		}
		fprintf(fp, "\n");
	}

	for(i=0; i<n; i++){
		fprintf(fp, "\t");
		for(j=0; j<n; j++){
			printf("Place the value of matrix b in [%d][%d]", i,j);
			scanf("%d", &b[i][j]);
			fprintf(fp, " %d", b[i][j]);
		}
		fprintf(fp, "\n");
	}
	return 0;
}
