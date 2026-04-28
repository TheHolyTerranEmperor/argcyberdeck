#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

//##getting this file started, its gonna need some work##
//setting up the boot script to begin, then we can get GUI going, lastly background functionality 

using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
    // Reading the Image
    Mat image = imread("/home/main/boot.jpeg",
                       IMREAD_COLOR);
    if (!image.data) {
        std::cout << "Could not open or "
                  << "find the image\n";
        return 0;
    }
    imshow("Output", image);
    waitKey(0);//wait for boot

    return 0;
}
