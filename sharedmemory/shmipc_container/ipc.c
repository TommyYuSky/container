#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <fcntl.h>
#include <sys/time.h>
#include <unistd.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <errno.h>
#include <mqueue.h>

#define Q_NAME	"/ch6_ipc"
#define MAX_SIZE 1024
#define M_EXIT	"done"
#define SRV_FLAG  "-producer"
#define MSG_NUM 10000000

int main(int argc, char *argv[])
{
	if (argc < 2)
	{
    	producer();
	}
	else if (argc >= 2 && 0 == strncmp(argv[1], SRV_FLAG, strlen(SRV_FLAG)))
	{
    	producer();
	}
	else
	{
    	consumer();
	}
}

int producer()
{
	const char *msg="test";	

	struct timeval stime;
	struct timeval etime;
	
	const char *name = "container";
	int shm_fd;
	void *ptr;
	void *ptr_s;
	int i, msg_len;
	
	/* open shared memory segment */
	shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666);
	
	/* set the size of shared memory segment */
	ftruncate(shm_fd, MAX_SIZE);
	
	/* now map the shared memory segment in the address space of the process */
	ptr = mmap(0, MAX_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
	
	if (ptr == MAP_FAILED){
		printf("mmap failed\n");
		return -1;
	}

	ptr_s = ptr;
	msg_len = strlen(msg);
	gettimeofday(&stime,NULL); 
	while (i < MSG_NUM)
	{
		//if (){
		//}
		sprintf(ptr,"%s",msg);
		//ptr += strlen(msg);	
    		i=i+1;
	}
	
	gettimeofday(&etime,NULL);
	long int diff_usec = 1000000 * (etime.tv_sec-stime.tv_sec) + etime.tv_usec-stime.tv_usec;
	long int diff_byte = MAX_SIZE*MSG_NUM;
	double throughput = diff_byte*8/diff_usec; // Megabyte
	printf("Time: %ld us\n",diff_usec);
	printf("Throughput: %f Gbits/s\n",throughput/1000);

	//sleep(1000);
 
	return 0;
}

int consumer()
{	
	struct timeval stime;
	struct timeval etime;
	
	const char *name = "container";
	int shm_fd;
	void *ptr;
	int i;
	long int len;
	
	shm_fd = shm_open(name, O_RDONLY, 0666);

	if (shm_fd == -1) {
    		printf("shm_open failed\n");
		exit(-1);
	}

	/* now map the shared memory segment in the address space of the process */
	ptr = mmap(0, MAX_SIZE, PROT_READ, MAP_SHARED, shm_fd, 0);
	if (ptr == MAP_FAILED) {
		printf("Map failed\n");
		exit(-1);
	}
	
	gettimeofday(&stime,NULL);
	int rmsg_num = 0; 
	do {
		//printf("%s", ptr);
		len = len + strlen(ptr);
		rmsg_num ++;
	} while (rmsg_num <= MSG_NUM);

	gettimeofday(&etime,NULL);
	long int diff_usec = 1000000 * (etime.tv_sec-stime.tv_sec) + etime.tv_usec-stime.tv_usec;
	long int diff_byte = MAX_SIZE*rmsg_num;
	double throughput = diff_byte*8/diff_usec; // Megabyte
	printf("len: %ld \n",len);
	printf("Byte: %ld MB;Time: %ld us; Msg number: %d\n",diff_byte/1000000,diff_usec,rmsg_num);
	printf("Throughput: %f Gbits/s\n",throughput/1000);

	/* remove the shared memory segment */
	if (shm_unlink(name) == -1) {
		printf("Error removing %s\n",name);
		exit(-1);
	}

	return 0;
}
