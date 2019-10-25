#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int fib(int n);


int main(){
	FILE *fp;
	int i, N;

	printf("N: ");
	scanf("%d", &N);
	fp= fopen("fibo.nacci", "w");
	for(i=0; i<N; i++){
	fprintf(fp, "fib(%d) = %d \n", i, fib(i));
	}
	fclose(fp);
	return 0;
}

int fib(int n){
	int x;
	if(n>1){
		x=fib(n-1)+fib(n-2);
		return x;	
	}
	else if(n==1) return 1;
	else if(n==0) return 0;
}
