import subprocess

# shell=True でやると インジェクションの余地が生まれる
# subprocess.run('dir .', shell=True)

# Win だと shell=True がないと実行されない？
r = subprocess.run(['dir'])
print(r.returncode)

# パイプするとき
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)
