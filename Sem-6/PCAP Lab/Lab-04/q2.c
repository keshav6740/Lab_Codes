#include <stdio.h>
#include <mpi.h>

#define N 3

int count_occurrences(int arr[], int size, int target) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            count++;
        }
    }
    return count;
}

int main(int argc, char *argv[]) {
    int rank, size, matrix[N][N], sub_matrix[N], element, local_count, global_count;
    
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0) {
        int temp[N * N] = {1, 2, 3, 3, 1, 2, 1, 1, 1};  
        element = 1;
        MPI_Bcast(&element, 1, MPI_INT, 0, MPI_COMM_WORLD);
        MPI_Scatter(temp, N, MPI_INT, sub_matrix, N, MPI_INT, 0, MPI_COMM_WORLD);
    } else {
        MPI_Bcast(&element, 1, MPI_INT, 0, MPI_COMM_WORLD);
        MPI_Scatter(NULL, N, MPI_INT, sub_matrix, N, MPI_INT, 0, MPI_COMM_WORLD);
    }

    local_count = count_occurrences(sub_matrix, N, element);
    MPI_Reduce(&local_count, &global_count, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        printf("Element %d appears %d times in the matrix.\n", element, global_count);
    }

    MPI_Finalize();
    return 0;
}
