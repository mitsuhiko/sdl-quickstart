#ifndef INC_%NAMESPACE%_GAME_HPP
#define INC_%NAMESPACE%_GAME_HPP

#include <%namespace%/%namespace%.hpp>


namespace %namespace% {

    void critical_error(const std::string &title,
                        const std::string &text);

    class game {
    public:
        game();
        ~game();

        SDL_Window *window() { return m_win; }
        SDL_GLContext glctx() { return m_glctx; }
        bool running() const { return m_running; }

        void mainloop();
        void update(float dt);
        void handle_event(SDL_Event &evt);
        void draw() const;
        void stop();

    private:
        SDL_Window *m_win;
        SDL_GLContext m_glctx;
        bool m_running;
    };
}

#endif
