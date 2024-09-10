import subprocess

def test_ccextractor(video_file_path, subtitle_file_path):
    command = [
        r'D:\ROhit N\Fatmug\backend\ccextractor\ccextractorwinfull.exe',
        video_file_path,
        '-o',
        subtitle_file_path,
        '--force'
    ]
    
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(f'Standard Output: {result.stdout}')
        print(f'Standard Error: {result.stderr}')
    except subprocess.CalledProcessError as e:
        print(f'Error occurred: {e}')
        print(f'Command Output: {e.output}')
        print(f'Command Error Output: {e.stderr}')
    except FileNotFoundError as e:
        print(f'FileNotFoundError: {e}')

if __name__ == '__main__':
    test_ccextractor()