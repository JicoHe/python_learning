# 没有通过函数修改列表的内容
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"printing model:{current_design}")
    completed_models.append(current_design)

print("The following designs are printed:")
for model in completed_models:
    print(model)

# 使用函数的，将程序分成两个过程，一个是打印，一个是显示
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing model:{current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    for model in completed_models:
        print(model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)