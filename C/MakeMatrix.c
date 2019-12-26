#include <stdio.h>
#include <math.h>

int main(){
	int i, j, n, m;
	
	
	printf("Give me the first dimension ");
	scanf("%d", &n);
	printf("Give me the second dimension ");
	scanf("%d", &m);

	int a[n][m], b[n][m];

	for(i=0; i<n; i++){
		for(j=0; j<m; j++){
			printf("Please enter the value for [%d][%d] ", i,j);
			scanf("%d", &a[i][j]);
			}
		}
	for(i=0; i<n; i++){
		for(j=0; j<m; j++){
			printf("And the value for [%d][%d] ", i,j);
			scanf("%d", &b[i][j]);
			}
		}
	printf("Alright, so your matrices are\n");

	for(i=0; i<n; i++){
		for(j=0; j<m; j++){
			printf("%d ", a[i][j]);
		}
		printf("\t");
		for(j=0; j<m; j++){
			printf("%d ", b[i][j]);
		}
		printf("\n");
	}
	printf("\n");
	return 0;
}

