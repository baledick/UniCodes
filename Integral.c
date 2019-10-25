#include <stdio.h>
#include <math.h>

int main(){
	double e, Prod, f, Prodn, fn, z;
	int i;

	e=0.5e-05;
	Prod=16.2;
	f=0.5;
	i=1;
	while(f>e){
		z=pow(-1,(i+2));
		Prodn=Prod*pow((5*3.14)+1/(2*(i+1)), (z*(i+1)));
		printf("O %d oros einai o: %lf \n", i, Prod);
		Prod=Prodn;
		fn=f/i;
		printf("I apostasi apo to e einai %lf \n", f-e);
		f=fn;
		
		
		printf("\n");
		i++;
	}
	return 0;
}
