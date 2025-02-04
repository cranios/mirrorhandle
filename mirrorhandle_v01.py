import maya.cmds as cmds

def copy_inner_to_outer_handles_mirror():
    # Seleciona as curvas animadas
    selected_curves = cmds.keyframe(query=True, name=True, selected=True)
    
    if not selected_curves:
        cmds.warning("Selecione pelo menos uma curva animada no Graph Editor.")
        return
    
    for curve in selected_curves:
        # Obtém os keyframes da curva
        keyframes = cmds.keyframe(curve, query=True, timeChange=True)
        
        for key in keyframes:
            # Obtém os valores das alças internas
            in_tangent = cmds.keyTangent(curve, query=True, time=(key,), inAngle=True)
            in_weight = cmds.keyTangent(curve, query=True, time=(key,), inWeight=True)
            
            # Define os valores das alças externas com os valores espelhados
            cmds.keyTangent(curve, edit=True, time=(key,), outAngle=-in_tangent[0], outWeight=in_weight[0])

def copy_outer_to_inner_handles_mirror():
    # Seleciona as curvas animadas
    selected_curves = cmds.keyframe(query=True, name=True, selected=True)
    
    if not selected_curves:
        cmds.warning("Selecione pelo menos uma curva animada no Graph Editor.")
        return
    
    for curve in selected_curves:
        # Obtém os keyframes da curva
        keyframes = cmds.keyframe(curve, query=True, timeChange=True)
        
        for key in keyframes:
            # Obtém os valores das alças externas
            out_tangent = cmds.keyTangent(curve, query=True, time=(key,), outAngle=True)
            out_weight = cmds.keyTangent(curve, query=True, time=(key,), outWeight=True)
            
            # Define os valores das alças internas com os valores espelhados
            cmds.keyTangent(curve, edit=True, time=(key,), inAngle=-out_tangent[0], inWeight=out_weight[0])

def create_ui():
    # Verifica se a janela já existe e a deleta
    if cmds.window("mirrorHandlesUI", exists=True):
        cmds.deleteUI("mirrorHandlesUI")
    
    # Cria a janela
    window = cmds.window("mirrorHandlesUI", title="Mirror Handles", widthHeight=(300, 200))
    
    # Cria um layout de coluna
    cmds.columnLayout(adjustableColumn=True)
    
    # Adiciona um texto informativo
    cmds.text(label="Selecione as curvas animadas no Graph Editor antes de usar os botões abaixo.")
    
    # Adiciona botões para executar os scripts
    cmds.button(label="Mirror Inner to Outer", command=lambda x: copy_inner_to_outer_handles_mirror())
    cmds.button(label="Mirror Outer to Inner", command=lambda x: copy_outer_to_inner_handles_mirror())
    
    # Adiciona um botão de fechar
    cmds.button(label="Fechar", command=lambda x: cmds.deleteUI(window))
    
    # Mostra a janela
    cmds.showWindow(window)

# Executa a função para criar a interface
create_ui()
