TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += \
        main.cpp
INCLUDEPATH += C:\Users\Bruker\armadillo-9.600.6\include
DEPENDPATH += C:\Users\Bruker\armadillo-9.600.6\include


LIBS += \
    -LC:\Users\Bruker\armadillo-9.600.6\examples\lib_win64 \
    -llapack_win64_MT \
    -lblas_win64_MT
