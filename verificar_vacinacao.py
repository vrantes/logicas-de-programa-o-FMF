def verificar_vacinacao():
    try:
        # Solicita a idade da criança primeiro para verificar a vacinação
        idade = int(input('Informe a idade da criança (em anos): '))

        # Verifica se a criança precisa de vacinação contra a gripe
        if idade < 5:
            print('A criança deve ser vacinada contra a gripe. Procure o posto de saúde mais próximo.')
        elif idade == 5:
            print('A vacina estará disponível em breve. Aguarde as próximas informações.')
        else:
            print('A vacinação só ocorrerá daqui a 3 meses. Informe-se novamente neste prazo.')

        # Solicita peso e altura da criança para avaliar o IMC
        peso = float(input('\nAgora informe o peso da criança (em kg): '))
        altura = float(input('Informe a altura da criança (em metros): '))

        # Calcula o IMC e fornece recomendações
        imc = peso / (altura ** 2)
        print(f'\nIMC da criança: {imc:.2f}')

        # Avalia o IMC e recomenda o especialista adequado
        if imc < 18.5:
            print('A criança está abaixo do peso. Considere consultar um pediatra especializado em nutrição ou um nutricionista infantil.')
        elif 18.5 <= imc < 24.9:
            print('A criança está com peso adequado. Continue acompanhando com o pediatra para garantir o crescimento saudável.')
        elif 25 <= imc < 29.9:
            print('A criança está acima do peso. É recomendável consultar um pediatra e um endocrinologista pediátrico para avaliação e orientação.')
        else:
            print('A criança está com obesidade. Procure um pediatra e, possivelmente, um endocrinologista e nutricionista infantil para acompanhamento intensivo.')

        print('\nCuide da saúde sempre. Até a próxima!')

    except ValueError:
        print('Erro: por favor, insira valores numéricos válidos para idade, peso e altura.')
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')

# Chama a função para executar o programa
verificar_vacinacao()

