#ifndef INC_%NAMESPACE%_%NAMESPACE%_HPP
#define INC_%NAMESPACE%_%NAMESPACE%_HPP

/* Include windows.h properly on Windows */
#if defined(WIN32) || defined(_WINDOWS)
#  define WIN32_LEAN_AND_MEAN
#  define NOMINMAX
#  include <windows.h>
#endif

/* SDL */
#include <SDL.h>
#include <SDL_opengl.h>
#define %namespace%_main main // avoid clashes, main() is a common word
#undef main

/* useful STL pieces */
#include <string>

#endif
