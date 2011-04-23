cmake_minimum_required(VERSION 2.6)
project(%projectname%)

# A list of header and source files used by your application.
set(SOURCES
    src/main.cpp
	src/game.cpp
)
set(HEADERS
	include/%namespace%/%namespace%.hpp
	include/%namespace%/game.hpp
)

# The following code finds SDL 1.3 in your checkout on OS X, Linux
# as well as Windows.  On Windows I am lazy and only look for the
# release version of SDL, feel free to make this also look for debug
# modes depending on the cmake build target.
set(SDL_FOLDER ${CMAKE_CURRENT_SOURCE_DIR}/libs/sdl-1.3
    CACHE STRING "Path to SDL 1.3" FORCE)
find_library(SDL_LIBRARY
    NAMES SDL-1.3.0 SDL
    PATHS ${SDL_FOLDER}
    PATH_SUFFIXES local/lib VisualC/SDL/Release
    NO_DEFAULT_PATH
)
find_library(SDLMAIN_LIBRARY
    NAMES SDLmain
    PATHS ${SDL_FOLDER}
    PATH_SUFFIXES local/lib VisualC/SDLmain/Release
    NO_DEFAULT_PATH
)

# we also need to find the system's OpenGL version
find_package(OpenGL REQUIRED)

# on OS X we also have to add '-framework Cocoa' as library.  This is
# actually a bit of an hack but it's easy enough and reliable.
set(EXTRA_LIBS "")
if (APPLE)
    set(EXTRA_LIBS ${EXTRA_LIBS} "-framework Cocoa")
endif()

# our own include folder and the SDL one are additional folders we
# want to have on our path.
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${SDL_FOLDER}/include
)

# Now we define what makes our executable.  First thing is the name,
# WIN32 is needed to make this a Win32 GUI application, MACOSX_BUNDLE
# activates bundle mode on OS X and the last two things are our source
# and header files this executable consists of.
add_executable(
    %projectname%
    WIN32
    MACOSX_BUNDLE
    ${SOURCES}
    ${HEADERS}
)

# Lastly we have to link the OpenGL libraries, SDL and the cocoa
# framework to our application.  The latter is only happening on
# OS X obviously.
target_link_libraries(
    %projectname%
    ${OPENGL_LIBRARIES}
    ${SDL_LIBRARY}
    ${SDLMAIN_LIBRARY}
    ${EXTRA_LIBS}
)

if(WIN32)
    set(VS_OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_CFG_INTDIR})
    add_custom_command(TARGET %projectname% POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        ${SDL_FOLDER}/VisualC/SDL/Release/SDL.dll ${VS_OUTPUT_DIR}/SDL.dll)
endif()
if(APPLE)
    set(BUNDLE_BINARY
        ${CMAKE_CURRENT_BINARY_DIR}/%projectname%.app/Contents/MacOS/%projectname%)
    add_custom_command(TARGET %projectname% POST_BUILD
        COMMAND python scripts/frameworkify.py ${BUNDLE_BINARY}
        ${SDL_LIBRARY})
endif()
