#include <stdio.h>

int main(){
	int i, j, position;
	double n, a[1000], min, sum1, sum2;
	i=1;
	printf("\nGive me a negative, non zero number: ");
	printf("\nOr insert 1 to continue");
	do{
		printf("\na[%d]= ", i);
		scanf("%lf", &n);
		if(n<0) a[i++]=n;
		else if(n==1) printf("Ending Programm...\n");
		else printf("I'm afraid I can't accept that.\n");
	}while(n != 1);
	
	min=a[1];
	sum1=0;
	sum2=0;

	for(j=1; j<=i; j++){
		sum1+= a[j]/(4*j);
		sum2+= a[j];
		if(a[j] <= min){
			min=a[j];
			position=j;
			}
		
	}
	printf("sum = %lf\n", sum1);
	printf("mean value = %lf\n", sum2/(i-1));
	printf("min = %lf, stin thesi: %d\n", min, position);
	printf("%d\n", i-1);
	return 0;
}
