platformer
==========

A simple and robust way to call a C compiler from Python. This used to be
a part of the PyPy project and got moved away. This example uses py.path.local
instances for path manipulation, refer to the pylib documentation for details.

Example usage:

    from platformer import platform, ExternalCompilationInfo, udir

    eci = ExternalCompilationInfo(includes=["math.h"])
    c_file = udir.join('x.c')
    c_file.write('int main() { printf("%f\\n", pow(2.0, 3.0)); return 0; }')
    exe_file = platform.compile([c_file], eci)
    res = platform.execute(exe_file)
    assert res.returncode == 0
    assert res.out.startswith('8.0')
