#include <iostream>
#include "clara.hpp"

int main(int argc, char * argv []) {
    int width = 0;
    auto cli = clara::Opt( width, "width" )
        ["-w"]["--width"]
        ("How wide should it be?");
    auto result = cli.parse( clara::Args( argc, argv ) );
    if( !result ) {
        std::cerr << "Error in command line: " << result.errorMessage() << std::endl;
        exit(1);
    }
    return 0;
}
