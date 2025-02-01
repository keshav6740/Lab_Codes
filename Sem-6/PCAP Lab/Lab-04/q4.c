#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mpi.h>

#define MAX_LEN 100

int main(int argc, char *argv[]) {
    int rank, size;
    char input_word[MAX_LEN];
    
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    
    if (rank == 0) {
        printf("Enter a word of length %d: ", size);
        fflush(stdout);
        scanf("%s", input_word);
        
        if (strlen(input_word) != (size_t)size) {
            printf("Error: The length of the input word must be %d.\n", size);
            MPI_Abort(MPI_COMM_WORLD, 1);
        }
    }
    
    MPI_Bcast(input_word, MAX_LEN, MPI_CHAR, 0, MPI_COMM_WORLD);
    char local_result[MAX_LEN];
    memset(local_result, 0, MAX_LEN);
    
    for (int i = 0; i < rank + 1; i++) {
        strncat(local_result, &input_word[rank], 1);
    }
    
    if (rank == 0) {
        gathered = (char *)malloc(MAX_LEN * size * sizeof(char));
        if (gathered == NULL) {
            fprintf(stderr, "Memory allocation failed on root process.\n");
            MPI_Abort(MPI_COMM_WORLD, 1);
        }
        memset(gathered, 0, MAX_LEN * size);
    }
    
    MPI_Gather(local_result, MAX_LEN, MPI_CHAR,
               gathered, MAX_LEN, MPI_CHAR, 0, MPI_COMM_WORLD);
    
    if (rank == 0) {
        char final_output[MAX_LEN * size];
        final_output[0] = '\0';  
        
        for (int i = 0; i < size; i++) {
            char *block = gathered + i * MAX_LEN;
            strcat(final_output, block);
        }
        printf("Output: %s\n", final_output);
        free(gathered);
    }
    
    MPI_Finalize();
    return 0;
}
