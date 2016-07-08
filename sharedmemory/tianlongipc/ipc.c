#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>
#include <unistd.h>
#include <sys/stat.h>
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
	struct timeval stime;
	struct timeval etime;
	mqd_t mq;
	struct mq_attr attr;
	char buffer[MAX_SIZE];
	int msg, i;

	attr.mq_flags = 0;
	attr.mq_maxmsg = 10;
	attr.mq_msgsize = MAX_SIZE;
	attr.mq_curmsgs = 0;

	mq = mq_open(Q_NAME, O_CREAT | O_WRONLY, 0644, &attr);

	/* seed random */
	srand(time(NULL));

	gettimeofday(&stime,NULL); 
	i = 0;
	while (i < MSG_NUM)
	{
    	// msg = rand() % 256;
	//msg = 888888;
    	//memset(buffer, 0, MAX_SIZE);
    	//sprintf(buffer, "%x", msg);
    	// printf("Produced: %s\n", buffer);
    	// fflush(stdout);
    	mq_send(mq, buffer, MAX_SIZE, 0);
    	i=i+1;
	}
	
	gettimeofday(&etime,NULL);
	long diff_usec = 1000000 * (etime.tv_sec-stime.tv_sec) + etime.tv_usec-stime.tv_usec;
	long diff_byte = MAX_SIZE*MSG_NUM;
	double throughput = diff_byte/diff_usec; // Megabyte
	printf("Time: %ld s\n",diff_usec/1000000);
	printf("Throughput: %f Mbs\n",throughput);
 
	memset(buffer, 0, MAX_SIZE);
	sprintf(buffer, M_EXIT);
	mq_send(mq, buffer, MAX_SIZE, 0);

	mq_close(mq);
	mq_unlink(Q_NAME);
	return 0;
}

int consumer()
{	
	struct timeval stime;
	struct timeval etime;
	struct mq_attr attr;
	char buffer[MAX_SIZE + 1];
	ssize_t bytes_read;
	mqd_t mq = mq_open(Q_NAME, O_RDONLY);
	if ((mqd_t)-1 == mq) {
    	printf("Either the producer has not been started or maybe I cannot access the same memory...\n");
    	exit(1);
	}
	
	gettimeofday(&stime,NULL);
	int rmsg_num = 0; 
	do {
    	bytes_read = mq_receive(mq, buffer, MAX_SIZE, NULL);
    	//buffer[bytes_read] = '\0';
	rmsg_num ++;
    	// printf("Consumed: %s\n", buffer);
	// } while (0 != strncmp(buffer, M_EXIT, strlen(M_EXIT)));
	} while (rmsg_num <= MSG_NUM);

	gettimeofday(&etime,NULL);
	long int diff_usec = 1000000 * (etime.tv_sec-stime.tv_sec) + etime.tv_usec-stime.tv_usec;
	long int diff_byte = MAX_SIZE*rmsg_num;
	double throughput = diff_byte/diff_usec; // Megabyte
	printf("Byte: %ld Mb;Time: %ld s; Msg number: %d\n",diff_byte/1000000,diff_usec/1000000,rmsg_num);
	printf("Throughput: %f Mbs\n",throughput);

	mq_close(mq);
	return 0;
}
