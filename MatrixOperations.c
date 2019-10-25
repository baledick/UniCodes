#include <stdio.h>
#include <math.h>

int main()
{
	int a[2][2], b[2][2], i, j;
	
	for(i=0; i<2; i++){
		for(j=0; j<2; j++){
			printf("Dwse mia timi tou pinaka ");
			scanf("%d", &a[i][j]);
		}
	}
	for(i=0; i<2; i++){
		for(j=0; j<2; j++){
			printf("Dwse mia timi tou pinaka ");
			scanf("%d", &b[i][j]);
		}
	}
	printf("\n");
	for(i=0; i<2; i++){
		for(j=0; j<2; j++){
			printf("%d ", a[i][j]);
		}
		printf("\t");
		for(j=0; j<2; j++){
			printf("%d ", b[i][j]);
		}
		printf("\n");
	}
	printf("\n");
	return 0;
}

