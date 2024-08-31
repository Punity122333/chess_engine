import subprocess

board_state = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPP/RNBQKNR w KQkq - 0 1"

subprocess.run(["g++","chessEngineCPP/engine.cpp","-o","engine"])

cpp_process = subprocess.Popen(["./engine"], stdin=subprocess.PIPE)

cpp_process.stdin.write(board_state.encode())
cpp_process.stdin.flush()
cpp_process.stdin.close()

cpp_process.wait()