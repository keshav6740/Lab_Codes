//even odd rank
#include <mpi.h>
#include <stdio.h>

int main(int argc, char* argv[]){
	int rank,size;
	int x = 5;

	MPI_Init(&argc, &argv);

	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	if (rank%2==0){printf("Rank: %d, Hello\n",rank);}
	else {printf("Rank: %d, World\n",rank);}
	MPI_Finalize();
	return 0;
}