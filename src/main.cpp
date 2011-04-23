#include <%namespace%/game.hpp>


int %namespace%_main(int argc, char **argv)
{
    // on windows we pin the mainloop to one processor in order to avoid
    // the performance hit of calling into the timing functions from
    // different processors and to avoid other timing related problems.
#if defined(WIN32) || defined(_WINDOWS)
    ULONG_PTR affinity_mask;
    ULONG_PTR process_affinity_mask;
    ULONG_PTR system_affinity_mask;

    if (!GetProcessAffinityMask(GetCurrentProcess(),
                                &process_affinity_mask,
                                &system_affinity_mask))
        return;

    // run on the first core
    affinity_mask = (ULONG_PTR)1 << 0;
    if (affinity_mask & process_affinity_mask)
        SetThreadAffinityMask(GetCurrentThread(), affinity_mask);
#endif

    %namespace%::game game;
    game.mainloop();
}
