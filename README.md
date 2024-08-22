<div align="center">

# DATAOPS PIPELINE


</div>

Projeto realizado durante ano letivo da Faculdade Impacta Tecnologia
 ---------------------------------------------------------------- 
**1. PROJETO DATAOPS** 
 ---------------------------------------------------------------- 
O projeto consiste em uma pipeline completa de DataOps, que abrange desde a *data ingestion* (Ingestão de dados) até a visualização e monitoramento dos dados. A proposta é desenvolver uma arquitetura robusta que implementa uma estrutura completa de DataOps com foco em automação, qualidade e governança dos dados.  

  ---------------------------------------------------------------- 

**1.1. Ferramentas**  
 ---------------------------------------------------------------- 
 

+ Análise para determinar o Data Source (streaming ou batch), por exemplo, arquivos dentro de um google drive.  

+ Linguagem Python e a ferramenta Pyspark de processamento para manipulação e leitura de dados para posteriormente os armazenar no Storage Cloud. 

+ Geração dos arquivos em horários específicos (schedule em batch). 

+ Apache Airflow ou Databricks para criação de jobs (leitura diária deste código, que pega as informações e as salva).  

+ Databricks para visualização de dados (visualização de tabelas e integração com Power BI).
  

 ----------------------------------------------------------------

**1.2. Tecnologias Utilizadas**   
 ---------------------------------------------------------------- 

+ Google Cloud Platform: irá gerenciar as ferramentas e o armazenamento de dados. 

+ Secret Key Manager: serviço responsável pela criptografia de chaves utilizadas em conexões de banco de dados ou qualquer outro acesso sensível, de forma que apenas pessoas autorizadas consigam acessa-los. 

+ Console: interação com a infraestrutura e as diversas ferramentas oferecidas pelo GCP. 

+ Compute Engine: provisionamento automático dos recursos necessários para utilização na infraestrutura e gerenciamento de máquinas virtuais. 

+ Databricks: integração com o GCP. Utilização do Databricks para integrar um repositório no GitHub, garantindo que o código esteja sempre salvo e versionado (relembrando os princípios de CI/CD), de modo a proporcionar facilidade na criação de notebooks, nos quais são possíveis se programar e agendar a execução de scripts. 

+ Storage GCP: armazenamento dos dados que serão trabalhados. Através do console, como criadores do projeto, estes possuem acesso direto para criar buckets e visualizar os dados armazenados. No entanto, é importante mencionar que, em um ambiente de organização, pode haver restrições de acesso direto ao lake de dados, por motivos de compliance e governança. 

+ Spark/Pyspark: desenvolvimento dos códigos da pipeline. 

+ Delta Table: liberdade na manipulação de tabelas, incluindo o histórico de versões e facilidade na alteração de esquemas. 

 ----------------------------------------------------------------

**1.3. Pré Requisitos** 
 ---------------------------------------------------------------- 
 

Antes de iniciar o projeto, vale mencionar algumas coisas que devem ser resolvidas de ante mão para evitar futuras dores de cabeça. Como pré-requisito, caso esteja trabalhando em um ambiente Windows, solicito que realize a instalação do “Git bash”, uma vez que ele será útil para a clonagem do repositório git na máquina local (aqui está o link para download: https://git-scm.com/downloads).  

Além disso, também solicito que instale o “Winutils.exe”. Esse software é um utilitário necessário para que o Apache Hadoop e suas dependências sejam executadas em sistemas Windows. Ele torna-se obrigatório quando Hadoop ou Apache Spark estão em cena, uma vez que esse programa lida com operações de sistema, como acesso a diretórios temporários e permissões de arquivos, que são, normalmente, realizados pelo Hadoop em sistemas Linux/Unix. Para utilizá-lo, basta seguir o passo a passo a seguir:  

1. Baixe a versão correspondente do winutils.exe para a versão do Hadoop que está sendo utilizada. Link para baixar: https://github.com/steveloughran/winutils 

2. Coloque o executável em uma pasta no seu sistema (C:\hadoop\bin\). Na aba de pesquisa do Windows, pesquise por: **Editar as variáveis de ambiente do sistema**. Após isso, clique em **variáveis de ambiente**.  Agora, clique em **novo**. Será aberto uma janela, no qual será solicitado um nome e um valor para essa variável. Como nome, coloque HADDO_HOME, enquanto para o valor, coloque este caminho: C:\hadoop. 

3. Por fim, agora basta baixar o Cygwin64 terminal. Este software será importante nos momentos de execução dos códigos no Vscode, já que o powershell padrão do Windows não possui suporte para comandos git. Para baixar o cygwin, basta ir neste link: https://www.cygwin.com/.  

Para instalar é muito simples, basta seguir os passos:  

1. Abra o arquivo que você baixou (setup-x86.exe ou setup-x86_64.exe). Clique em **Next** para iniciar o processo de instalação. Escolha o diretório onde você quer instalar o Cygwin (por exemplo, C:\cygwin). Clique em **Next**. 

2. Escolha um diretório temporário onde os arquivos de instalação serão salvos. Pode ser algo como C:\cygwin\packages. Clique em **Next**. 

3. Selecione o método de conexão com a internet. Normalmente, a opção **Direct Connection** funciona para a maioria dos usuários. Clique em **Next**. 

 

4. Selecione um mirror da lista. Os mirrors são servidores que hospedam os pacotes de instalação. Escolha um que esteja próximo da sua localização para downloads mais rápidos. Clique em **Next**. 

 

5. Na tela de seleção de pacotes, no campo de busca, digite zsh (esse será o terminal usado no Vscode). Encontre o pacote zsh e clique na coluna **Skip** para selecionar a versão que deseja instalar. Isso alterará o texto de Skip para a versão do Zsh que será instalada. 

 

6. Clique em Next para **prosseguir**. O instalador baixará e instalará o Zsh junto com quaisquer dependências necessárias. Após a conclusão do download e instalação, clique em **Finish**. 

 

7. Agora que o Cygwin foi instalado com o pacote zsh, é necessário que o zhs seja o shell padrão.  

 

8. Abra o Cygwin. Execute o seguinte comando "/bin/zsh" para iniciar o Zsh manualmente. Isso iniciará o Zsh, permitindo que as configurações necessárias sejam feitas dentro do shell Zsh. 

 

9. Para definir o Zsh como shell padrão, é necessário editar o arquivo de configuração de inicialização do shell padrão atual. Geralmente, isso é feito no arquivo ".bashrc" ou ".bash_profile" do seu diretório home. Execute o comando "nano ~/.bashrc" para abrir o arquivo no editor de texto padrão (use nano ou vim conforme sua preferência): 

 

10. Por fim, adicione a seguinte linha ao final do arquivo: "exec /bin/zsh -l". Agora Salve o arquivo e saia do editor (Ctrl + X e depois Y para salvar no nano). 

 

11. Para verificar se está tudo certo, feche o terminal do Cygwin e abra-o novamente. O Zsh deve iniciar automaticamente, indicando que ele agora é o shell padrão. No Zsh, pode-se verificar qual shell está em uso executando "echo $SHELL" (o resultado deve mostrar /bin/zsh, confirmando que o Zsh é o shell padrão). 

 

12. Para finalizar, colocaremos o cygwin zsh como shell utilizável no Vscode. Com o Vscode aberto, acesse as configurações. Clique em **File** (Arquivo) no menu superior e selecione **Preferences** (Preferências), depois escolha **Settings** (Configurações). Alternativamente, você pode usar o atalho de teclado Ctrl + vírgula (,) para abrir as configurações diretamente. 

 

13. Na parte superior direita da aba de configurações, você verá um ícone de documento com uma seta (parece um ícone de abrir arquivo). Clique nesse ícone para abrir as configurações no modo JSON. Se não conseguir ver o ícone, certifique-se de que você está na visualização de configurações e procure pela opção Open Settings (JSON). 

 

14. Uma vez no modo JSON, você verá um arquivo de configurações chamado "settings.json". Procure a seção correspondente a "terminal.integrated.profiles.windows" ou adicione a seção abaixo, se ainda não existir: 

 

 
```
{ 
    "terminal.integrated.defaultProfile.windows": "Cygwin Zsh", 
    "terminal.integrated.profiles.windows": { 
        "Cygwin Zsh": { 
            "path": "C:\\cygwin64\\bin\\zsh.exe", 
            "args": ["-l"], 
            "env": { 
                "CHERE_INVOKING": "1" 
            } 
        } 
    } 
} 
```

 

15. Certifique-se de que o caminho C:\\cygwin64\\bin\\zsh.exe está correto para o seu sistema. Ajuste conforme necessário para o diretório onde o Cygwin está instalado. Após fazer as alterações necessárias, salve o arquivo usando Ctrl + S. 

----------------------------------------------------- 

**1.4.  Montando o Projeto**  
 ---------------------------------------------------------------- 
Para executar o meu projeto corretamente, recomendo criar uma conta no Google Cloud Platform (GCP), caso ainda não tenha, e seguir os passos de configuração e execução abaixo. A documentação do projeto contém todas as etapas para reproduzir algo semelhante ao meu setup, mas o essencial é configurar a conta, importar o arquivo e rodar no ambiente preparado. 

Após criar a conta no GCP, um projeto será criado automaticamente. Para facilitar o gerenciamento, vamos renomeá-lo. No canto superior direito, próximo à sua foto de perfil, clique no menu e vá até **Configurações do Projeto**. Lá, você poderá renomear o projeto; eu escolhi "Databricks with GCP", mas você pode escolher o nome que preferir. 

<div align="center">
  
![Acessando configurações](https://github.com/user-attachments/assets/1240ef7e-6683-41f9-8994-0057e261c497)
  
  imagem 1 - Acessando configurações 
</div>  
  


 <div align="center">

![Alterando nome do projeto e salvando](https://github.com/user-attachments/assets/e50158c6-9910-4aa1-9b13-44a40f7df794)

  imagem 2 - Alterando nome do projeto e salvando 

 </div>

Após renomear o projeto, ativaremos o Databricks. No canto superior esquerdo, há uma barra de menu. Acesse-a e procure pelo Databricks. O GCP permite fixar essa opção para facilitar o acesso no futuro, o que recomendo fazer. 

 <div align="center">

 ![Databricks fixado](https://github.com/user-attachments/assets/b8cdd5eb-db69-43ef-a1fe-54de02fc53de)

  imagem 3 - Databricks fixado 
</div>
 

Depois de acessar o Databricks, clique em "**Assinar**" e aceite os termos e condições. Antes de confirmar, você verá um resumo do plano gratuito, incluindo o período de teste. 

Um detalhe importante: você precisará cadastrar um cartão de crédito para fins de faturamento. No entanto, não se preocupe, o Google não fará cobranças automáticas sem sua autorização. Quando o período de teste acabar, se você não optar por um plano pago, os recursos serão automaticamente desativados sem gerar custos. 

<div align="center">

![Resumo do pedido, ao assinar o Databricks](https://github.com/user-attachments/assets/bed04270-2d95-4ebc-87bd-72dfce6add3e)

imagem 4 - Resumo do pedido, ao assinar o Databricks 
</div>
 

Faça login com a conta usada no GCP e selecione o plano sugerido para criar sua conta no Databricks. Uma tela aparecerá solicitando o nome da organização; escolha o nome que preferir 

<div align="center">
 
![Criando conta](https://github.com/user-attachments/assets/4427d3c6-3c81-4a1a-b536-fc0105b04b0c)

imagem 5 - Criando conta 
</div>
 

Após completar esse processo, você receberá um e-mail de confirmação. 

 <div align="center">
   
![Exemplo e-mail](https://github.com/user-attachments/assets/d8a5fccb-07e9-450d-879a-b6037cc42f88) 

imagem 6 - Exemplo e-mail 
</div>
Quando o e-mail chegar, volte ao console do GCP na aba do Databricks. Clique em "Gerenciar no fornecedor", que redirecionará você para criar seu workspace. Faça login novamente, selecione o plano de assinatura e confirme. 

<div align="center">
  
 ![Gerenciar no fornecedor](https://github.com/user-attachments/assets/9d2a4798-15ba-42de-bcaf-11c5cf1afa86)

  imagem 7 - Gerenciar no fornecedor 
</div>
 
<div align="center">

 ![Plano de assinatura](https://github.com/user-attachments/assets/de07738d-ce11-46e1-9c7b-60a3e82d4628)

  imagem 8 - Plano de assinatura 
</div>
 

 Agora que os passos anteriores foram concluídos, será aberto o Workspace no Databricks. Contudo, antes de criar o espaço de trabalho, criaremos o repositório no git hub para assim criar o Workspace. 

<div align="center">

 ![criando repositório](https://github.com/user-attachments/assets/865be5c1-de69-435a-9473-1dbca5fbbaee)

Imagem 9 – Criando repositório no Git 
</div>

<div align="center">

![clone do git](https://github.com/user-attachments/assets/b372e699-a874-477f-91ab-d171628c4f00)

Imagem 10 – Pegando o Link do repositório 
</div>
 

Agora que foi criado a conta no git, será criado o Worksplace no Databricks 

<div align="center">
 
![create workspace](https://github.com/user-attachments/assets/d3f49b91-7133-4721-a28f-f0c00f16ece8)

Imagem 11 – Local para criar o Workspace 
</div>
 
 <div align="center">
   
![criando workspace](https://github.com/user-attachments/assets/f1f0e6a9-0fef-401e-8e48-df6d2386d146)

Imagem 12 - Criando Workspace 

</div>

 ---------------------------------------------------------------

 

1.4.1. CI/CD GitHub e Databricks 
-----------------------------------------------------------
 

Neste projeto iremos realizar a conexão entre Github e Databricks, para CI/CD. Primeiro vamos conectar o nosso repositório. Depois de criar o ambiente de trabalho basta clicar no workspace (ou no link) que irá redirecionar para uma página dentro desse ambiente. Agora dentro do espaço de trabalho, iremos conectar um repositório git (por isso que ele foi criado anteriormente) 

<div align="center">

 ![criando repositório no db](https://github.com/user-attachments/assets/e4ef1470-046a-4c5f-96b4-3320f919381a)

Imagem 13 – Criando git folder 
</div>

<div align="center">
	
 ![criando repositório no db2](https://github.com/user-attachments/assets/18252f72-8af7-4ff7-866e-94a17afffc10)

Imagem 14 – Conectando o repositório git no Databricks 
</div>
 

Agora que o repositório foi conectado ao Databricks, será preparado o ambiente no Vscode (criação das pastas que irão armazenar o projeto git). Porém, antes disso, devemos realizar a clonagem do repositório git em nossa máquina. Para realizar a clonagem, basta seguir as instruções desse site: 

https://www.alura.com.br/artigos/clonando-repositorio-git-github 

 

Agora que o repositório foi criado, iremos preparar a estrutura de diretórios e em seguida baixar a base de dados que se encontra no site da Kaggle (basta entrar neste link e baixar) 

https://www.kaggle.com/datasets/alphiree/cardiovascular-diseases-risk-prediction-dataset?select=CVD_cleaned.csv  

 

Quanto a estrutura, basta seguir o mesmo padrão apresentado pela imagem a seguir 

 
<div align="center">
	
 ![ambiente no vscode](https://github.com/user-attachments/assets/58a25e47-1681-4112-93cf-1508cf704800)

 Imagem 15 – Estrutura no Vscode 
</div>
 

Vale dizer que o arquivo CSV deverá ser colocado dentro do diretório “data_source”. Além disso, também deve ser dito que o arquivo “requirements.txt”, aparecerá após a execução deste comando no terminal:  
```
Pip freeze > requirements.txt 
```
Por fim, também é interessante dizer que é sempre importante trabalhar utilizando a máquina virtual. Para isto, basta digitar o seguinte comando no terminal: 

```
python3 –m venv venv 
```
---------------------------------------------------------------------------------------------------------- 

1.4.2. Github Actions 
-------------------------------------------------------------
Para implementar nossa esteira de integração e entrega contínua, vamos utilizar os workflows do GitHub. Eles garantirão a consistência do código, evitando futuros erros e simplificando a depuração, o que melhora a experiência de todos os usuários que colaboram no repositório.  

O primeiro workflow que vamos implementar, seguindo os princípios de DataOps, é o Lint. Ele é responsável por verificar se a estrutura e a escrita do código estão corretas, prevenindo possíveis erros antes que o código seja integrado e executado. No exemplo abaixo, o Ruff é instalado ou atualizado e, em seguida, é utilizado para realizar o linting em todos os arquivos. Uma coisa deve ser dita, o código a seguir deve ser salvo como um arquivo .yml (por exemplo: build_pylint.yml) dentro do diretório workflows. 
```
name: Pylint

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Lint with Ruff
      run: |
        pip install ruff
        ruff --format=github --target-version=py37 .
      continue-on-error: true
```
 

Agora que finalizamos a criação do nosso pipeline, o próximo passo é subir as atualizações do nosso repositório Git. Primeiramente, devemos executar o comando **git add .**, que irá preparar todas as mudanças realizadas para o commit. Em seguida, é importante rodar o comando **git status** para verificar quais arquivos foram modificados e estão prontos para serem comitados. Esses comandos serão executados no terminal do Visual Studio Code. Para registrar as mudanças, realizaremos um commit utilizando o comando **git commit -m "Recriando pastas e build"**, o que adiciona uma mensagem descritiva sobre o que foi alterado. Assim, essas informações serão registradas na branch atual. Finalmente, vamos executar o comando **git push** para enviar todas as atualizações para o repositório remoto, garantindo que as alterações fiquem sincronizadas no GitHub ou outra plataforma de versionamento que esteja sendo utilizada. 

 

<div align="center"> 

 ![build](https://github.com/user-attachments/assets/9e0834b8-1d6f-4fb6-9b67-b643faeabd3a)
 
Imagem 16 – Verificando a build 
</div>
 
------------------------------------------------------------------------

1.4.3. ELT/ETL 
-----------------------------------------------------------------------
Agora que já subimos a build, realizamos os commits e confirmamos que tudo foi corretamente versionado, o próximo passo é fazer o pull no Databricks. Isso garantirá que tanto o ambiente local quanto o Databricks estejam sincronizados, com ambos possuindo os mesmos arquivos atualizados. 

 
<div align="center">
 
![realizando o pull](https://github.com/user-attachments/assets/89693956-047d-45cf-b028-1d815c04210e)


Imagem 17 – Caminho para Pull 
</div>
 
<div align="center">

 ![pull](https://github.com/user-attachments/assets/1614a1c5-26c1-4cc1-b9f0-93e9f7eb0eec)


Imagem 18 - Criação de pull request 

</div> 

<div align="center">

![pull realizad](https://github.com/user-attachments/assets/b0782bb7-5e8c-4c31-887b-29f4c60ca74a)

Imagem 19 – Pull realizado 

 </div>

Depois da pull ser realizada, criaremos uma compute que servirá como uma infraestrutura de processamento no qual os notebooks, jobs e pipelines serão executados.  


<div align="center">
	
 ![criando compute](https://github.com/user-attachments/assets/26c1149e-7dd9-4619-834b-0b05353ba4f0)

Imagem 20 - Criando cluster 
</div>

<div align="center">
 
![configurando compute](https://github.com/user-attachments/assets/4d0048c1-10e8-47a3-ab96-a54985327d82)

Imagem 21 - Configurando cluster 
</div>

 

Agora que a compute já está rodando, será criada uma ingestão dentro do notebook. Para isso, basta clicar em criar no canto superior direito, e ir em “Notebook”. Vale ressaltar que isso deve ser feito dentro do notebook que está na pasta **src**.  

<div align="center">

 ![Criando notebook](https://github.com/user-attachments/assets/8cba34ff-8e15-43ec-88bb-2cbdaca0da92)


Imagem 22 – Criando Notebook 
</div>
 

Agora que o notebook foi criado, antes de começarmos a desenvolver os códigos necessários, precisamos acessar o Google Cloud Storage e fazer o upload do arquivo CSV. No meu projeto, esse arquivo está nomeado como cardiovascular.csv. Esse passo é essencial para garantir que os dados estejam disponíveis para serem utilizados no notebook durante a implementação. Para encontrar, no GCP, as coisas realizadas no notebook, basta seguir o caminho mostrado na imagem. Vale destacar que o uso de pastas temporárias é uma boa prática ao trabalhar com arquivos no ambiente cloud. O motivo é simples e intuitivo: não é recomendável fazer o upload direto dos arquivos para o console do Google Cloud Platform (GCP). Organizar esses arquivos em diretórios temporários permite um controle maior e evita poluir o ambiente principal com arquivos que não precisam ser armazenados de forma permanente. 

<div align="center">

![localizando pastas criadas na ingestão](https://github.com/user-attachments/assets/c5331526-3350-4116-a860-679425639c2b)


Imagem 23 – Caminho até a pasta 
</div>
 
<div align="center">

![fazendo upload no GCP](https://github.com/user-attachments/assets/e5252ec1-1a9d-4332-92c4-94b704ecaacf)


Imagem 24 – Fazendo o Upload 

</div> 

Após a criação do notebook e o upload dos arquivos no Google Cloud Storage, o próximo passo é configurar o Databricks para acessar esses arquivos. Para isso, será necessário criar uma credencial de armazenamento no Databricks e, em seguida, configurar um local externo que permita ao Databricks acessar os arquivos armazenados na nuvem.  

Para criar a credencial de armazenamento no Databricks, siga os passos abaixo: 

1. Acesse a aba **Catálogo** no Databricks. 

2. No canto superior direito, clique no ícone de **engrenagem**. 

3. Selecione a opção **Credenciais de Armazenamento**. 

4. Na nova tela, clique em **Criar Credencial**, localizada no canto superior direito. 

5. Na janela que aparecerá, você deverá preencher o tipo da credencial, o nome e um comentário opcional. 

6. Após preencher as informações necessárias, clique em **Criar** para finalizar o processo. 

Com isso, sua credencial de armazenamento estará configurada e pronta para uso. Com a credencial de armazenamento já criada no Databricks, o próximo passo é configurar as permissões no Google Cloud Platform (GCP) para permitir a conexão entre o Databricks e o Google Cloud. Para isso: 

1. Acesse o Google Cloud e navegue até **Cloud Storage**. 

2. Dentro do Cloud Storage, selecione a opção **Permissões**. 

3. Clique em **Permitir Acesso** para abrir a tela de configuração de permissões. 

4. Na nova tela, adicione os participantes inserindo o e-mail associado à credencial de armazenamento criada no Databricks. Esse e-mail pode ser encontrado na tela de criação da credencial, na parte inferior. 

5. Na seção **Atribuir Papéis**, selecione as permissões adequadas para que o Databricks possa acessar os arquivos no Cloud Storage (neste ponto, você especificaria as permissões exatas, como 'Leitor de Objetos' ou 'Administrador de Objetos', por exemplo). 

Ao configurar corretamente essas permissões, a integração entre o Databricks e o Google Cloud Storage estará pronta para uso. Com a credencial de armazenamento criada e configurada, o próximo passo é criar o local externo no Databricks. Para isso: 

1. No Databricks, acesse a aba **Catálogo**. 

2. No canto superior direito, clique na **engrenagem** e selecione **Localizações Externas**. 

3, Uma nova aba será aberta. Clique em **Criar Localização**. 

4. Na tela de criação da nova localização externa, você deverá fornecer as seguintes informações: 

   - Nome da Localização:  Nome apropriado para a nova localização externa. 

   - Credencial de Armazenamento: Credencial que criada anteriormente. 

   - URL: Insira o caminho completo (caminho absoluto) para acessar o local de armazenamento na nuvem. 

5. Para encontrar a URL correta no Google Cloud Storage, acesse o Google Cloud Storage e selecione o bucket desejado. 

6. Navegue pelo explorador de pastas até localizar a pasta e o arquivo específicos (no caso, o arquivo 'cardiovascular'). 

7. A URL completa pode ser obtida ao clicar no arquivo e copiar o caminho absoluto. 

Com essas informações preenchidas corretamente, o local externo estará configurado no Databricks, permitindo o acesso aos arquivos armazenados na nuvem.  

<div align="center">

![f](https://github.com/user-attachments/assets/06c8339d-1ac2-4bfc-a5f7-bec71e322c8b)



Imagem 25 – Pegando caminho absoluto 
</div>
 

Com todos os pré-requisitos finalmente configurados, podemos iniciar o processo de ETL. No notebook do Databricks, basta executar os comandos descritos na imagem a seguir para começar a ingestão de dados.  

 

 

 <div align="center">


![ingestão](https://github.com/user-attachments/assets/f81c213c-4817-4a12-a412-3ec1750e5dc7)



Imagem 26 - Ingestão ELT 
</div>
 

É importante destacar que o comando display é específico para o ambiente do Databricks. Caso estivéssemos trabalhando em um ambiente Python local, seria necessário instalar algumas bibliotecas adicionais para obter funcionalidades semelhantes. Nesse caso, você precisaria rodar: 

  
```
pip install databricks 

pip install pyspark 
```
  

No ambiente Python, ao invés do comando display, você utilizaria o método show() ou outra função equivalente para visualizar os dados. Isso garante que você tenha a flexibilidade de executar o processo ETL tanto no Databricks quanto em um ambiente Python tradicional 



<div align="center">

![extração](https://github.com/user-attachments/assets/5019452b-e96b-416c-b85f-b9a0428aafd7)

 
Imagem 27 - Extração  
</div>
 
<div align="center">

![delta location](https://github.com/user-attachments/assets/46da7ef0-f5dc-4883-90d6-1b0173c69c5a)


Imagem 28 – Load e criação do Database 
</div>
 

Algumas ressalvas importantes precisam ser mencionadas: 

  

- **Criação da Pasta Temporária**: Essa pasta, responsável por armazenar o arquivo CSV, pode ser criada tanto pelo ambiente em nuvem quanto diretamente através dos comandos no notebook. No meu caso, durante a construção do projeto, optei por criar a pasta diretamente no notebook, pois considerei essa abordagem mais prática. 

 

- **Armazenamento dos Dados (Load)**: Durante o processo de load dos dados, no momento de salvar, você define o caminho onde os dados serão armazenados. Foi nesse ponto que criei a pasta para armazenar o arquivo cardiovascular. 

 

- **Especificidade do Caminho no Comando SQL**: Ao criar a tabela no Databricks usando um comando SQL, onde o LOCATION exige o caminho absoluto, precisei inserir o caminho completo, incluindo todas as pastas, por estar utilizando um ambiente Windows. Esse detalhe foi necessário no meu caso, embora, em uma aula que assisti, a profissional responsável pelo conteúdo não precisou inserir o caminho completo. Isso demonstra que o comportamento pode variar de acordo com o ambiente de execução. 

 

Com o notebook já criado, o próximo passo é configurar um job de execução no Databricks. Para isso: 

1. Na aba **Data Engineering**, clique em **Execução de Jobs**. 

2. Em seguida, selecione **Criar Job**. 

3. Preencha os campos necessários conforme as imagens a seguir demonstram. 

As imagens mostrarão detalhadamente o passo a passo para a criação do job, garantindo que todos os parâmetros sejam configurados corretamente. 

<div align="center">

![criando job](https://github.com/user-attachments/assets/4afc67b5-60d0-4e3f-981a-fcb1e9ed995f)
	
 
 Imagem 29 – Criando Job 
</div>
 
<div align="center">

![criando jobb](https://github.com/user-attachments/assets/8ead09d0-bb1b-4bd6-9db6-b1a081fa23b9)


Imagem 30 – Configurando job 
</div>
 
-----------------------------------------------------------------------------------------------------------

1.4.4. Chave de Autenticação 
----------------------------------------------------------------------------------------------------------
Para deixar o projeto mais profissional e seguro, uma boa prática é configurar uma chave SSH. A seguir, está um guia simplificado sobre como criar uma chave SSH pelo terminal do VS Code: 

Antes de criar a chave de autenticação, devemos ativar o serviço ssh.  

1. Abra o Gerenciador de Serviços: 

2. Pressione Win + R, digite services.msc e pressione Enter. 

3. Encontre o serviço "OpenSSH Authentication Agent": 

4. Clique com o botão direito sobre o serviço e selecione **Propriedades**. 

5. No campo Tipo de Inicialização, altere para **Automático**. 

6. Em seguida, clique em **Iniciar** para ativar o serviço. 

7. Clique em "**Aplicar**" e "**OK**". 

8. Agora que ele está ativo, podemos digitar os códigos. Digite o seguinte comando no terminal do Vsco:  

```
ssh-keygen -t rsa -b 4096 -C "seu_email@example.com" 
``` 

Esse comando cria uma chave RSA com um tamanho de 4096 bits, que é uma configuração recomendada para garantir a segurança. O terminal solicitará que você escolha um local para salvar a chave. Por padrão, ele sugerirá salvar em **~/.ssh/id_rsa**. Agora só aceitar o local padrão ou especificar um caminho diferente. Além disso, também pode-se definir uma senha para a chave SSH. Se preferir não usar uma senha, basta pressionar Enter duas vezes. Para garantir que sua chave SSH seja usada automaticamente ao se conectar a repositórios Git, adicione a chave ao ssh-agent: 

``` 

eval "$(ssh-agent -s)" 

ssh-add C:\Users\seu_usuario\.ssh\id_rsa 
 
```

Para copiar o conteúdo da chave, basta digitar o seguinte comando: 

 
```
cat C:\Users\seu_usuario\.ssh\id_rsa.pub 

(Esse comando irá exibir a chave, bastando o adicionar à sua conta no GitHub) 
```
<div align="center">

![z](https://github.com/user-attachments/assets/784d1bb2-56f6-4813-a0de-d5726d5fb6ac)


Imagem 31 - Comandos no Powershell 
</div>
  

Por fim, basta adicionar a chave ao Github. Para isso, no GitHub, devemos ir em **Configurações** (Settings) > **SSH and GPG keys**. Clique em **New SSH key**. Cole a chave pública no campo "Key" e dê um nome para ela em "Title". Clique em **Add SSH key**.  

 

 <div align="center">

 ![a](https://github.com/user-attachments/assets/f83f8d57-8837-453c-a1fc-9f7cf8bcbe25)


Imagem 32 – Adicionando chave  

 </div>

 
<div align="center">

 ![1](https://github.com/user-attachments/assets/ac0b5eb0-39e4-4aac-b0fc-97ad7eb72e73)


Imagem 33 – Chave criada 
</div>
 

Essa configuração aumenta significativamente a segurança do projeto ao garantir que apenas dispositivos autorizados possam acessar os repositórios através da chave SSH. 

Para integrar o Databricks com o GitHub, precisamos gerar um token de acesso pessoal (PAT - Personal Access Token) e configurá-lo no Databricks. Esse processo permite criar branches, realizar operações de leitura e escrita, e integrar essas ações com nossa esteira de integração e entrega contínua (CI/CD). 

 

**Gerando o Token de Acesso Pessoal (PAT)**: 

1. No GitHub, acesse **Configurações** (Settings). 

2. Em seguida, vá para **Configurações de Desenvolvedor** (Developer settings). 

3. Escolha a opção **Tokens de acesso pessoal** (Personal access tokens) e selecione **Generate new token** (classic). 

4. Defina as permissões necessárias para o token, como: 

	- repo: para controle total sobre os repositórios (criação de branches, commits, etc.). 

	- workflow: se for necessário interagir com GitHub Actions. 

**Adicionar o Token ao Databricks**: 

1. No ambiente do Databricks, acesse a seção de Configurações de Integração com Git. 

2. Adicione o token gerado no campo apropriado. Isso permitirá a autenticação para realizar operações como criação de branches, commits e outras interações com o repositório. 

**Integração com a Esteira CI/CD**: 

1. Após configurar o token, você poderá fazer push de mudanças do Databricks para o repositório GitHub. 

2. Quando um push for realizado, o workflow configurado no GitHub Actions será acionado, executando a build e validando o código de acordo com as regras definidas. 

**Monitoramento e Visualização**: 

1. Após cada push, será possível visualizar o status do build diretamente no GitHub Actions, acompanhando a execução da esteira CI/CD e garantindo a qualidade e integração contínua do projeto. 

 ------------------------------------------------------------------------

1.4.5. Testes com Pyspark e Data Quality 
--------------------------------------------------------------------

Após passarmos pelos processos iniciais do DataOps, chegamos a um dos pilares mais importantes: o Data Quality. Esse conceito envolve garantir a qualidade dos dados e implementar testes para assegurar a confiabilidade das informações. 

Na prática, o código desenvolvido no notebook do Databricks foi consolidado em um arquivo .py no VS Code, chamado cardiovascular.py. Esse processo envolve redigitar o código do notebook no arquivo Python, com algumas adaptações necessárias para que ele funcione corretamente no ambiente local. As alterações específicas serão demonstradas  a seguir. 

```

# Databricks notebook source.
# MAGIC %md
# MAGIC #Ingestão de Dados ELT
# MAGIC Conjunto de dados de previsão de risco de doenças cardiovasculares

# COMMAND ------------

display(dbutils.fs)

# COMMAND ------------

display(dbutils.fs.ls("/"))

# COMMAND ------------

dbutils.fs.mkdirs("/tmp/")

# COMMAND -------------

display(dbutils.fs.ls("/"))

# COMMAND -------------

display(dbutils.fs.ls("/tmp/"))

# COMMAND -------------

# MAGIC %md
# MAGIC # Extraindo dados/Realizando a leitura

# COMMAND ------------

df = spark.read.format("csv").option("header", True).load("dbfs:/tmp/cardiovascular.csv")

# COMMAND ------------

df.display()

# COMMAND ------------

df.select("General_Health").distinct().display()

# COMMAND ------------

df.printSchema()

# COMMAND ------------

# MAGIC %md
# MAGIC # Rename Cols

# COMMAND ------------

df = df.withColumnRenamed("Height_(cm)", "Height_cm").withColumnRenamed("Weight_(kg)", "Weight_kg")

# COMMAND ------------

# MAGIC %md
# MAGIC # Realizando o armazenamento de dados

# COMMAND ------------

df.write.format("delta").mode("overwrite").option("mergeSchema", True).partitionBy("General_Health").save("/hospital/rw/suus/cardiovascular/")

# COMMAND ------------

# MAGIC %md
# MAGIC # Criando database e tabela pelo delta location;

# COMMAND ------------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS db_hospital;

# COMMAND ------------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS db_hospital.cardiovascular_diseasess LOCATION "gs://databricks-46083817904810/46083817904810/hospital/rw/suus/cardiovascular";

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando detalhes da tabela criada

# COMMAND ------------

# MAGIC %sql
# MAGIC select * from db_hospital.cardiovascular_diseasess;
     
# COMMAND ------------

# MAGIC %sql
# MAGIC desc detail db_hospital.cardiovascular_diseasess;
     
# COMMAND ------------

# MAGIC %sql
# MAGIC desc detail delta.`gs://databricks-46083817904810/46083817904810/hospital/rw/suus/cardiovascular`;

# COMMAND ------------

# MAGIC %md
# MAGIC # Analisando dados

# COMMAND ------------

df = spark.table("db_hospital.cardiovascular_diseasess")
     
# COMMAND ------------

df.count()

# COMMAND ------------

df.show(10, False)

# COMMAND ------------     

df.display()

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando classificação de saúde cardiovascular
# MAGIC Pesquisa de como as pessoas classificam a sua saúde do coração

# COMMAND ------------

df.groupby("General_Health", "Sex").count().display()

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando a quantidade de pessoas que tiveram frequência no hospital

# COMMAND ------------

df.groupBy("Checkup", "Age_Category").count().distinct().display()

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando quem faz atividade fisica

# COMMAND ------------

df.groupBy("Exercise", "Sex").count().display()

# COMMAND ------------

# MAGIC %md
# MAGIC # Verificando quem teve doença cardíaca coronária ou infarto do miocárdio

# COMMAND ------------

df.groupBy("Heart_Disease", "Sex").count().display()

# COMMAND ------------     

df.groupBy("Heart_Disease", "Age_Category").count().display()


```

 

Além disso, para executar o código no ambiente local, é preciso garantir que as bibliotecas necessárias estejam instaladas. Isso inclui rodar os seguintes comandos no terminal: 

```
pip install delta-spark 

pip install pyspark 
```
 

Ao final desse processo, teremos um código adaptado para rodar no notebook do Databricks. Com relação a buid primeira era focada em pylint, mas agora vamos reescrever a build para que ela suporte o processo de CI (Continuous Integration). 
--------------------------------------------------------------------------
1.4.5.1. Pipeline de ETL 
------------------------------------------------------------------------
Pipeline de ETL (Extract, Transform, Load) que realiza a ingestão, transformação e armazenamento de dados usando Spark e Delta Lake.  

```
import logging
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
from pathlib import Path


def setup_session():
    builder = SparkSession.builder.appName("Ingestão Cardio") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.hadoop.io.nativeio.enabled", "false") \
        .config("spark.hadoop.fs.native.enabled", "false") \
        .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0")

    return configure_spark_with_delta_pip(builder).getOrCreate()


def read_csv(spark, path=None):
    if path is None:
        path = Path("data_sources") / "cardiovascular.csv"
    else:
        path = Path(path)

    logging.info("Realizando leitura do arquivo no caminho: %s", path)

    if not path.exists():
        raise FileNotFoundError(f"O arquivo não foi encontrado no caminho especificado: {path}")

    df = spark.read.format("csv").option("header", "true").load(str(path))
    df.show(truncate=False)  # Imprime o DataFrame na tela
    return df


def rename_columns(df):
    logging.info("Renomeando colunas")
    return df.withColumnRenamed("height_(cm)", "height_cm").withColumnRenamed("Weight_(kg)", "Weight_kg")


def save_delta(df, output_path=Path("storage/hospital/rw/cardiovascular/")):
    logging.info("Armazenando dados")
    return df.write.format("delta").mode("overwrite").option("mergeSchema", "true").partitionBy("General_Health").save(str(output_path))


def main():
    spark = setup_session()
    absolute_path = "C:/Projeto_DataOps/Dataops.Pipiline/data_sources/cardiovascular.csv"
    df = read_csv(spark, absolute_path)
    df = rename_columns(df)
    save_delta(df)
    spark.stop()


if __name__ == "__main__":
    main()  # dessa vez vai

``` 



**Importações**: 

- logging: Para registrar logs, como mensagens de informação e erros. 

- SparkSession: Classe principal do Spark para criar a sessão de trabalho. 

- Delta: Utilizado para integrar o Delta Lake com o Spark. 

- Path: Facilita o manuseio de caminhos de arquivos. 

- Função setup_session():Configura e retorna uma sessão Spark, habilitada para trabalhar com Delta Lake. 

- Define o nome da aplicação: "Ingestão Cardio". 

- Configura extensões e catálogos para trabalhar com o Delta Lake. 

- Define a dependência do Delta Lake usando o pacote delta-core_2.12:2.4.0. 

 

**Função read_csv(spark, path=None)**: 
 

- Lê um arquivo CSV, com um caminho padrão se nenhum for especificado. 

- Verifica se o caminho existe; se não, lança uma exceção. 

- Carrega os dados em um DataFrame Spark e os exibe. 

- Retorna o DataFrame para ser usado nas próximas etapas. 

**Função rename_columns(df)**: 

- Renomeia as colunas do DataFrame para remover caracteres especiais, como parênteses, para padronizar o formato dos nomes. 

- Função save_delta() 

- Salva o DataFrame em formato Delta, particionado pela coluna General_Health, no caminho especificado. 

- Usa o modo overwrite, que substitui os dados existentes. 

- A opção mergeSchema permite adicionar novas colunas caso a estrutura do DataFrame mude. 

 

**Função main()**: 

- Esta função é o ponto de entrada principal. 

- Cria a sessão Spark. 

- Lê os dados do arquivo CSV especificado. 

- Realiza a transformação de renomear colunas. 

- Salva os dados no formato Delta no diretório de saída especificado. 

- Finaliza a sessão Spark. 

**Execução do Script**: 

- Garante que o script só será executado se for chamado diretamente. 

- De forma geral, esse script faz a leitura de um arquivo CSV contendo dados de saúde cardiovascular, transforma as colunas para padronizar os nomes e armazena os dados no formato Delta, que permite armazenamento eficiente e consultas rápidas. Tudo isso é integrado em uma sessão Spark configurada para trabalhar com Delta Lake. O fluxo de trabalho envolve leitura, transformação e gravação dos dados. 
--------------------------------------------------------------------------------------------------------------------------------
1.4.5.2. Testes unitários 
-------------------------------------------------------------------------------------------------------------------------------
O seguinte código é um conjunto de testes unitários que validam diferentes partes do pipeline de ETL, garantindo que ele funcione corretamente mesmo em cenários de falha. Ele cobre a leitura, transformação e salvamento dos dados, além de tratar possíveis exceções e erros que podem ocorrer durante o processo 
```
import shutil
import unittest
import logging
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType
from src.hospital.ingestion_cardiovascular import read_csv, rename_columns, save_delta
from pathlib import Path


class PySparkTest(unittest.TestCase):

    @classmethod
    def suppress_py4j_logging(cls):
        logger = logging.getLogger("py4j")
        logger.setLevel(logging.WARN)

    @classmethod
    def create_testing_pyspark_session(cls):
        builder = SparkSession.builder \
            .appName("Testes Pyspark") \
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        spark = configure_spark_with_delta_pip(builder).getOrCreate()
        return spark

    @classmethod
    def setUpClass(cls):
        cls.suppress_py4j_logging()
        cls.spark = cls.create_testing_pyspark_session()

    @classmethod
    def tearDownClass(cls):
        storage_test_path = Path("tests/storage_test")
        if storage_test_path.exists() and storage_test_path.is_dir():
            shutil.rmtree(storage_test_path)
        cls.spark.stop()

    @staticmethod
    def dataframe_mock(spark):
        schema = StructType([
            StructField("General_Health", StringType(), True),
            StructField("Checkup", StringType(), True),
            StructField("Exercise", StringType(), True),
            StructField("Heart_Disease", StringType(), True),
            StructField("Skin_Cancer", StringType(), True),
            StructField("Other_Cancer", StringType(), True),
            StructField("Depression", StringType(), True),
            StructField("Diabetes", StringType(), True),
            StructField("Arthritis", StringType(), True),
            StructField("Sex", StringType(), True),
            StructField("Age_Category", StringType(), True),
            StructField("Height_cm", DoubleType(), True),
            StructField("Weight_kg", DoubleType(), True),
            StructField("BMI", DoubleType(), True),
            StructField("Smoking_History", StringType(), True),
            StructField("Alcohol_Consumption", DoubleType(), True),
            StructField("Fruit_Consumption", DoubleType(), True),
            StructField("Green_Vegetables_Consumption", DoubleType(), True),
            StructField("FriedPotato_Consumption", DoubleType(), True)
        ])

        data = [
            ("Excellent", "Within the past 2 years", "Yes", "No", "No", "No", "No", "No",
             "No", "Female", "70-74", 152.0, 52.16, 22.46, "No", 0.0, 30.0, 4.0, 0.0),
            ("Excellent", "Within the past year", "Yes", "No", "No", "No", "No", "No",
             "Yes", "Male", "70-74", 191.0, 112.49, 31.0, "No", 0.0, 30.0, 10.0, 15.0)
        ]

        return spark.createDataFrame(data, schema)

    def test_read_csv(self):
        df = read_csv(self.spark)
        self.assertIsNotNone(df)
        self.assertEqual(df.count(), 308854)

    def test_rename_columns(self):
        data = PySparkTest.dataframe_mock(self.spark)
        renamed_df = rename_columns(data)
        self.assertListEqual(renamed_df.columns, ["General_Health", "Checkup", "Exercise", "Heart_Disease", "Skin_Cancer", "Other_Cancer", "Depression", "Diabetes", "Arthritis", "Sex",
                             "Age_Category", "Height_cm", "Weight_kg", "BMI", "Smoking_History", "Alcohol_Consumption", "Fruit_Consumption", "Green_Vegetables_Consumption", "FriedPotato_Consumption"])

    def test_save_delta(self):
        data = PySparkTest.dataframe_mock(self.spark)
        path = Path("tests/storage_test")
        save_delta(data, path)

    def test_fail_read_csv(self):
        path = ""
        with self.assertRaises(Exception):
            read_csv(self.spark, path)

    def test_fail_rename_columns_with_invalid_type(self):
        data = PySparkTest.dataframe_mock(self.spark)
        df_invalid = data.withColumn("Weight_kg", data["Weight_kg"].cast(StringType()))

        df_renamed = rename_columns(df_invalid)
        self.assertTrue(isinstance(df_renamed.schema["Weight_kg"].dataType, StringType))

    def test_fail_save_delta(self):
        schema = StructType([
            StructField("Name", StringType(), True),
            StructField("Height", IntegerType(), True),
            StructField("Weight", DoubleType(), True)
        ])
        data = [("Alice", 170, 60.5)]
        df = self.spark.createDataFrame(data, schema)

        with self.assertRaises(Exception):
            rename_columns(data)
            save_delta(df)


if __name__ == '__main__':
    unittest.main()  # suus
```

**Importações**: 

- shutil: Para manipular diretórios, como remover diretórios de teste. 

- unittest: Framework de testes integrado ao Python. 

- logging: Para controle de logs. 

- SparkSession e configure_spark_with_delta_pip: Para criar a sessão Spark e configurar o Delta Lake. 

- StructType e StructField: Para definir esquemas de DataFrames de teste. 

- read_csv, rename_columns, save_delta: Funções sendo testadas, importadas do módulo onde o pipeline está implementado. 

**Classe PySparkTest(unittest.TestCase)**: 

- Define a classe de testes, herdeira de unittest.TestCase. 

 

 

**Métodos de Configuração**: 

- Suprime logs desnecessários da biblioteca Py4J, que o PySpark utiliza. 

- Cria uma sessão Spark configurada para Delta Lake, usada nos testes. 

- Configura a sessão Spark antes de rodar os testes. 

- Após os testes, remove o diretório de teste, se existir, e encerra a sessão Spark. 

**Mock de DataFrame**: 

- Cria um DataFrame de teste com um esquema específico para simular o comportamento dos dados reais. 

**Testes Unitários**: 

- Teste de leitura de CSV: Testa se o arquivo CSV é lido corretamente e valida o número de registros. 

- Teste de renomeação de colunas: Valida se as colunas foram renomeadas corretamente. 

- Teste de salvamento em Delta Lake: Testa se os dados são salvos corretamente no formato Delta. 

**Testes de falha**: 

- Falha ao ler CSV: Testa se o código lida corretamente com a ausência de um caminho válido. 

- Falha ao renomear colunas com tipo inválido: Testa se o código lida com tipos de dados incorretos. 

- Falha ao salvar em Delta Lake: Testa se o código lança exceções corretamente ao tentar salvar um DataFrame incompatível. 

 

**Execução dos Testes**: 

- Executa todos os testes quando o script é rodado diretamente. 

 
----------------------------------------------------------------------------------------
1.4.6. Visualização de dados  
---------------------------------------------------------------------------------------
A visualização de dados (ou Data Visualization), consiste na prática de representar os dados em gráficos ou em tabelas, de modo a facilitar o entendimento a respeito do que essas informações conseguem nos passar. A visualização de dados é essencial para o projeto, pois, por meio dela, conseguimos encontrar padrões nos dados, definir tendências e obter insights interessantes.  

Para a finalização do projeto, decidi utilizar a criação de dashboards que o próprio databricks oferece, já que sua inferface é intuitiva e de fácil entendimento. A seguir mostrarei alguns gráficos criados e o que suas informações nos passam.  


<div align="center">
 
![grafico](https://github.com/user-attachments/assets/c905b2d0-1cc5-43db-9bfb-ca001bedd70e)

Imagem 34 - Dashboard 
</div>
 

<div align="center">

 ![g](https://github.com/user-attachments/assets/c74c7331-b782-4ac5-834a-03dc3e124b2b)


Imagem 35 – Dashboard II 

</div>

<div align="center">

![la](https://github.com/user-attachments/assets/0403115e-18fd-4f79-94f5-13b8576fe0da)

Imagem 36 – Dashboard III 

</div>


<div align="center">

![tabe](https://github.com/user-attachments/assets/eb75edaf-3127-4668-a67e-5c12c03cbbdb)


Imagem 37 – Dashboard IV 
</div>

**Distribuição de Doenças Cardiovasculares e Prática de Exercícios Físicos** 

 

O gráfico superior esquerdo mostra a relação entre a presença de doenças cardiovasculares e a prática de exercícios físicos. Nota-se que a maior parte dos indivíduos que não possuem doenças no coração também não praticam exercícios, com um número significativo de pessoas (223.414) que fazem exercícios regularmente e não têm doenças cardíacas. Já entre aqueles que possuem doenças cardíacas, a proporção de pessoas que não praticam exercícios é maior (60.469), comparado àqueles que praticam (15.967). Isso sugere uma correlação potencial entre a prática de exercícios e a saúde cardíaca. 

**Prática de Atividades Físicas por Sexo** 

O gráfico inferior esquerdo aborda a prática de atividades físicas dividida por sexo. Ambos os sexos têm uma distribuição similar em termos de prática de atividades físicas. Para os que não praticam atividades, há uma ligeira predominância de mulheres (39.858) sobre homens (29.615). Entre aqueles que praticam atividades físicas, os números são quase equivalentes entre os sexos, com mulheres (120.338) e homens (119.043) participando quase na mesma proporção. 

 

**Saúde Geral e Prática de Exercícios** 

A saúde geral dos indivíduos é apresentada no gráfico inferior direito e o gráfico superior direito. Há uma clara tendência de que pessoas que avaliam sua saúde como "Very Good" ou "Good" tendem a praticar exercícios físicos, enquanto aqueles que avaliam sua saúde como "Poor" têm uma menor adesão à prática de atividades físicas. Isso destaca a importância do exercício regular para a manutenção de uma boa saúde geral. 

**Distribuição de Saúde Geral por Sexo** 

Os gráficos mostram que tanto homens quanto mulheres se distribuem de maneira similar em relação à avaliação de sua saúde. No entanto, observa-se uma ligeira superioridade de homens em avaliações "Very Good" (52.518 homens contra 57.877 mulheres) e "Good", sugerindo que, de uma forma geral, homens podem estar mais inclinados a considerar sua saúde como melhor. 

**Distribuição por Sexo** 

O gráfico de pizza mostra a distribuição geral dos sexos, com uma leve predominância feminina (51,87%) em comparação à masculina (48,13%). Isso deve ser levado em consideração na análise, pois pode influenciar os números absolutos apresentados nos gráficos anteriores. 

 

**Relação entre Saúde Geral e Diabetes** 

Os dados apresentados mostram que indivíduos que relatam uma saúde geral "Very Good" tendem a não ter diabetes, o que pode indicar uma forte correlação entre a percepção de boa saúde e a ausência de diabetes. Por outro lado, aqueles que classificam sua saúde como "Poor" mostram uma maior incidência de diabetes, destacando uma possível relação negativa entre o controle glicêmico e a saúde percebida. 

 

**Peso Corporal e Saúde Geral** 

 

Os dados revelam uma variação significativa no peso corporal entre indivíduos com diferentes percepções de saúde. Aqueles que consideram sua saúde como "Very Good" têm pesos que variam amplamente, mas permanecem dentro de uma faixa mais saudável em comparação com aqueles que relatam uma saúde "Poor", onde observamos pesos mais elevados, como 125,65 kg. Esse fato pode indicar que o peso excessivo está associado a uma pior avaliação da saúde geral. 

**Consumo de Frutas e Verduras** 

Indivíduos com saúde "Very Good" apresentam um consumo consistente de frutas e verduras, com alguns consumindo até 30 porções de frutas e 60 porções de verduras verdes. Em contrapartida, aqueles com saúde "Poor" têm um consumo drasticamente reduzido desses alimentos, com alguns relatando consumir apenas 2 porções de frutas e 1 porção de verduras verdes. Esses dados sugerem que uma dieta rica em frutas e verduras pode estar fortemente associada a uma melhor saúde geral. 

**Implicações Gerais** 

A análise dos dados e gráficos evidencia a importância de uma abordagem integrada para a manutenção de uma boa saúde geral, destacando o papel fundamental de uma dieta equilibrada e da prática regular de exercícios físicos. Os dados indicam que indivíduos que mantêm uma alimentação rica em frutas e verduras, além de controlar o peso, tendem a relatar melhor saúde e apresentam menor incidência de doenças crônicas como diabetes. Além disso, a prática regular de atividades físicas está associada a uma melhor percepção da saúde e a uma menor ocorrência de doenças cardíacas. Observa-se também que essas práticas saudáveis são benéficas para todos os grupos, independentemente do sexo. Assim, intervenções focadas na promoção de hábitos alimentares saudáveis e na atividade física regular são essenciais para a prevenção de doenças crônicas e para a melhoria da qualidade de vida. 



 ------------------------------------------------------------

**2. ARQUITETURA UTILIZADA COMO BASE DE ESTUDO** 
--------------------------------------------------------

<div align="center">
	
 ![Arquitetura ](https://github.com/user-attachments/assets/79999527-747b-4ec9-90bf-5968dcf05bb1)


Imagem 56 – Arquitetura base 
</div>

Seu funcionamento, explicação a respeito das tecnologias e ferramentas utilizadas foram apresentas no início deste documento.  
