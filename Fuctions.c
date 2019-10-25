#include <stdio.h>
#include <math.h>
#include <stdlib.h>

long double a(int n);

long double a0, a1;

int main(){
	int N, i;
	FILE *fp;
	fp = fopen("data.txt", "w");	
	printf("Dwse moy tis times twn a0, a1 ");
	scanf("%Le, %Le", &a0, &a1);
	printf("Dwse mou ton arithmo twn vimatwn ");
	scanf("%d", &N);
	for(i=0; i<N; i++){
		fprintf(fp, "a(%d)=%Le\n", i, a(i));
	}
	fclose(fp);
	return 0;
}

long double a(int n){

	long double x, y;
	if (n > 1){
		x=sqrt((sin(a(n-1))+exp(n))/(40+a(n-2)));
		return x;
	}
	else if(n == 1) return a1;
	else if(n == 0) return a0;
	else if(n < 0) printf("Oxi");
}
