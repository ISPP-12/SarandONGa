def user_info(request):
    usuario_logeado = request.user.is_authenticated
    if usuario_logeado:
        perteneciente_a_VidesSur = request.user.ong.name == 'VidesSur'
    else:
        perteneciente_a_VidesSur = False

    return {
        'usuario_logeado': usuario_logeado,
        'perteneciente_a_VidesSur': perteneciente_a_VidesSur,
    }
