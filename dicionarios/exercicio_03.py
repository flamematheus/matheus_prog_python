import os
os.system("cls")

escola ={
    "aluno_001":{
        "nome":"ana silva",
        "idade":20,

        "notas":{
            "matematica":8.5,
            "portugues":9.8,
            "historia":7.5
            },
        "contato":{
            "email":"ana@gmail.com",
            "telefone":"1199885465"
            
        }
        

    }
    
}

print(escola["aluno_001"]["notas"]["matematica"])