#include <%namespace%/game.hpp>
#include <iostream>

static const int window_width = 800;
static const int window_height = 600;
static const float simulation_dt = 0.01f;


void %namespace%::critical_error(const std::string &title,
                                   const std::string &text)
{
#if defined(WIN32) || defined(_WINDOWS)
    MessageBoxA(0, text.c_str(), title.c_str(),
        MB_OK | MB_SETFOREGROUND | MB_ICONSTOP);
#else
    std::cout << "Critical error: " << title << std::endl << text << std::endl;
#endif
    exit(1);
}

%namespace%::game::game()
{
    if (SDL_Init(SDL_INIT_VIDEO) < 0)
        %namespace%::critical_error("Could not initialize SDL", SDL_GetError());

    SDL_GL_SetAttribute(SDL_GL_MULTISAMPLEBUFFERS, 1);
    SDL_GL_SetAttribute(SDL_GL_MULTISAMPLESAMPLES, 4);
    SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);
    SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24);
    SDL_GL_SetAttribute(SDL_GL_RED_SIZE, 8);
    SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE, 8);
    SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE, 8);
    SDL_GL_SetAttribute(SDL_GL_ALPHA_SIZE, 8);

    m_win = SDL_CreateWindow("Hello SDL",
        SDL_WINDOWPOS_CENTERED,
        SDL_WINDOWPOS_CENTERED,
        window_width, window_height,
        SDL_WINDOW_OPENGL | SDL_WINDOW_SHOWN);
    if (!m_win)
        %namespace%::critical_error("Unable to create render window", SDL_GetError());

    m_glctx = SDL_GL_CreateContext(m_win);
    SDL_GL_SetSwapInterval(1);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0.0f, window_width, window_height, 0.0f, -1.0f, 1.0f);

    glMatrixMode(GL_MODELVIEW);

    m_running = true;
}

%namespace%::game::~game()
{
    SDL_GL_DeleteContext(m_glctx);
    SDL_DestroyWindow(m_win);
    SDL_Quit();
}

void %namespace%::game::mainloop()
{
    SDL_Event evt;
    uint64_t old_ticks = 0;
    float accumulator = 0.0f;

    while (m_running) {
        uint64_t now = SDL_GetPerformanceCounter();
        float dt = (now - old_ticks) / (float)SDL_GetPerformanceFrequency();
        old_ticks = now;

        // this took way too long.  We probably had a suspended mainloop
        // (debugger, window moved etc.)
        if (dt > 0.1f)
            dt = simulation_dt;

        while (SDL_PollEvent(&evt))
            handle_event(evt);

        // run the simulation at a fixed frequency.
        accumulator += dt;
        while (accumulator >= simulation_dt) {
            update(simulation_dt);
            accumulator -= simulation_dt;
        }

        draw();
        SDL_GL_SwapWindow(m_win);

        // wait a little bit so that our timer has enough precision in the
        // worst case scenario.  This also yields to other processes.
        SDL_Delay(1);
    }
}

void %namespace%::game::update(float dt)
{
}

void %namespace%::game::handle_event(SDL_Event &evt)
{
    if (evt.type == SDL_QUIT)
        stop();
}

void %namespace%::game::draw() const
{
    glClearColor(0.3f, 0.6f, 0.9f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);
}

void %namespace%::game::stop()
{
    m_running = false;
}
