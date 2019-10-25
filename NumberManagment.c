#include <stdio.h>

int main(){
	int i, j, position;
	double n, a[1000], min, sum1, sum2;
	i=1;
	printf("\nDwse enan arnitiko mh mideniko arithmo: ");
	printf("\nDwse 1 gia na vgeis");
	do{
		printf("\na[%d]= ", i);
		scanf("%lf", &n);
		if(n<0) a[i++]=n;
		else if(n==1) printf("Termatismos programmatos\n");
		else printf("Den mporw na to dextw\n");
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
	printf("mesi timi = %lf\n", sum2/(i-1));
	printf("min = %lf, stin thesi: %d\n", min, position);
	printf("%d\n", i-1);
	return 0;
}
