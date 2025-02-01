#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

#define N 4  // Matrix is 4x4

int main(int argc, char *argv[]) {
    int rank, size;
    int matrix[N][N];  
    int row[N];         

    MPI_Init(&argc, &argv);                     
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);       
    MPI_Comm_size(MPI_COMM_WORLD, &size);     

    if (size != N) {
        if (rank == 0)
            printf("Error: This program requires exactly %d processes.\n", N);
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    if (rank == 0) {
        printf("Enter %d integers for a %dx%d matrix (row by row):\n", N * N, N, N);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                scanf("%d", &matrix[i][j]);
            }
        }
    }

    MPI_Scatter(matrix, N, MPI_INT, row, N, MPI_INT, 0, MPI_COMM_WORLD);
    for (int j = 0; j < N; j++) {
        row[j] += j + rank;
    }

    int result_matrix[N][N];
    MPI_Gather(row, N, MPI_INT, result_matrix, N, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        printf("Transformed matrix:\n");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                printf("%d ", result_matrix[i][j]);
            }
            printf("\n");
        }
    }

    MPI_Finalize();  // Finalize MPI
    return 0;
}
