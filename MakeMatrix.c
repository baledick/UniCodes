#include <stdio.h>
#include <math.h>

int main(){
	int i, j, n, m;
	
	
	printf("Dwse mou tin prwti diastasi tou pinaka ");
	scanf("%d", &n);
	printf("Dwse mou tin deuteri diastasi tou pinaka ");
	scanf("%d", &m);

	int a[n][m], b[n][m];

	for(i=0; i<n; i++){
		for(j=0; j<m; j++){
			printf("Dwse mou tin timi [%d][%d] ", i,j);
			scanf("%d", &a[i][j]);
			}
		}
	for(i=0; i<n; i++){
		for(j=0; j<m; j++){
			printf("Dwse mou tin timi [%d][%d] ", i,j);
			scanf("%d", &b[i][j]);
			}
		}
	printf("Teleia, ara oi pinakes sou einai oi\n");

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

