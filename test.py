이번 챕터에서 배운 커맨드들을 정리해볼게요.

git init : 현재 디렉토리를 Git이 관리하는 프로젝트 디렉토리(=working directory)로 설정하고 그 안에 레포지토리(.git 디렉토리) 생성
git config user.name 'codeit' : 현재 사용자의 아이디를 'codeit'으로 설정(커밋할 때 필요한 정보)
git config user.email 'teacher@codeit.kr' : 현재 사용자의 이메일 주소를 'teacher@codeit.kr'로 설정(커밋할 때 필요한 정보)
git add [파일 이름] : 수정사항이 있는 특정 파일을 staging area에 올리기
git add [디렉토리명] : 해당 디렉토리 내에서 수정사항이 있는 모든 파일들을 staging area에 올리기 
git add . : working directory 내의 수정사항이 있는 모든 파일들을 staging area에 올리기
git reset [파일 이름] : staging area에 올렸던 파일 다시 내리기
git status : Git이 현재 인식하고 있는 프로젝트 관련 내용들 출력(문제 상황이 발생했을 때 현재 상태를 파악하기 위해 활용하면 좋음) 
git commit -m "커밋 메시지" : 현재 staging area에 있는 것들 커밋으로 남기기
git help [커맨드 이름] : 사용법이 궁금한 Git 커맨드의 공식 메뉴얼 내용 출력
앞으로 각 챕터에서 새롭게 배운 커맨드들은 이렇게 정리하고 넘어가겠습니다.


==> github에 repository 만들고 , local에서 올림
$ git remote add origin https://github.com/mwgoh/MathTool.git
$ git branch -M main
$ git push -u origin main

local repository => Remote repository로 
$ git push  수행

Remote repository => local repository
$ git pull 

여기서 upstream 은 로컬과 연결된 원격 저장소를 의미해용
즉 git push --set-upstream A B 를 하게 되면 로컬 A 저장소의 원격저장소를 B 로 지정하여 B 에 
push 하라는 의미에용
이렇게 이 명령을 한번 하게 되면 이제 원격저장소는 B 가 되기 때문에 다시 push 할 때 
--set-upstream 을 쓰지 않아도 됩니당

$ git remote -v  -> remote 리스트 확인

원칙적으로 자신의 리모트 레포지토리에는 자신만 git push를 할 수 있습니다. 
만약 다른 사용자도 git push를 할 수 있게 해주려면 그 사용자를 해당 리모트 레포지토리의 collaborator로 지정하면 됩니다. 

=====================>
이전 영상에서는 내용을 수정한 파일 중에서 커밋에 반영하고 싶은 파일은 git add를 해야한다고 했습니다. 그런데 사실 이것과 관련해서 꼭 알아야할 사실이 하나 있습니다. 이 사실을 확실히 이해하고 암기해야 앞으로 깃을 사용할 때 어려움이 없습니다. 자, 그럼 설명할게요.
Git은 내부적으로 크게 3가지 종류의 작업 영역을 두고 동작합니다.

각 작업 영역의 이름은
working directory
staging area
repository입니다. 순서대로 하나씩 설명해드릴게요.

첫 번째 작업 영역인 working directory는 작업을 하는 프로젝트 디렉토리를 말합니다. 그러니까 지금 상황에서는 MathTool 디렉토리가 working directory입니다.
두 번째 작업 영역인 staging area는 git add를 한 파일들이 존재하는 영역입니다. 커밋을 하게되면 staging area에 있는 파일들만 커밋에 반영됩니다.
세 번째 작업 영역인 repository는 working directory의 변경 이력들이 저장되어 있는 영역입니다. 그러니까 커밋들이 저장되는 영역이라는 뜻인데요. 조금 풀어서 설명해볼게요.

working directory에서 뭔가 작업을 하고,
작업한 파일들을 git add 해주고,
커밋을 하면 staging area에 있던 파일들의 모습이 마치 영화의 한 장면, 스냅샷(snapshot)처럼 이 repository에 저장되는 겁니다.
그리고 '02. repository 만들기' 영상에서 본 것처럼 실제로는 MathTool 디렉토리 안에 숨겨져 있던 .git 디렉토리가 repository입니다.

3가지 작업 영역이 잘 이해되시나요? 좀더 잘 이해하기 위해 다음 그림을 봅시다.

왼쪽부터 순서대로 working directory, staging area, repository가 있습니다. 다음과 같은 작업을 한 상태를 나타내는 그림인데요.

working directory에서 A.txt 파일과 B.txt 파일을 작성하고 
git add A.txt와 git add B.txt를 실행해서 A.txt, B.txt 둘다 staging area에 올렸습니다.
그 다음 git commit -m "Ver_1"를 실행해서 staging area에 있는 파일들을 가져와 커밋으로 남겼습니다. 
Git에서 커밋을 할 때 어떤 식으로 일이 진행되는 건지 좀 이해되시죠?

자, 작업을 좀더 해볼까요?
이전 그림에서 작업을 좀더 하고 나서의 모습인데요. 다음과 같은 작업을 추가적으로 했습니다.

working directory에서 A.txt 파일 내용에 Python~이라는 단어를 추가, B.txt 파일 내용에 Morning!이라는 단어를 추가했습니다. 
그런데 이번에는 git add B.txt만 실행해서 B.txt 파일만 staging area에 올렸습니다. 
그 다음 git commit -m "Ver_2"로 두 번째 커밋을 했습니다. 
이전 그림과 다른 점은 A.txt는 staging area에 올리지 않고, B.txt만 staging area에 올렸다는 점입니다. 그랬더니 지금 repository에서 그 결과가 어떤가요? 
Ver_2 커밋을 보면 지금

A.txt는 staging area에 있던 모습, 그러니까 수정하기 이전의 모습이 Ver_2 커밋에 반영되었고
B.txt도 staging area에 있던 모습, 하지만 A.txt와는 달리 수정한 이후의 모습이 Ver_2 커밋에 반영되었습니다.
A.txt, B.txt 둘다 working directory에서 수정했다는 사실은 같지만, staging area에 올렸는지 여부에 따라 그 최신 모습이 커밋에 반영되는지가 달라지는 겁니다. 
바로 이 점이 Git을 사용할 때 잘 알고 기억해야하는 부분입니다.

그런데 staging area가 굳이 왜 필요할까요? working directory에서 작업을 하고 git add할 필요없이 바로 커밋해버리는 구조가 더 편할 것 같은데 말이죠. 
하지만 꼭 그렇지는 않습니다. 방금처럼 A.txt와 B.txt 파일을 둘다 수정했더라도 두 파일 모두 그 최신 모습을 다음 커밋에 반영하고 싶지 않을 수도 있습니다. 
방금처럼 B.txt의 최신 모습만 그 다음 커밋에 반영하고 싶을 수도 있는 거죠. 이런 상황은 실제로 꽤 자주 있습니다. 만약 staging area가 없다면 원하는 것들만 
선별적으로 커밋에 반영할 수 없게 됩니다. 그럼 좀더 세밀한 버전 관리를 할 수 없게 되는 거죠. 왜 staging area가 필요한지 알겠죠?

자, 이때까지 Git의 3가지 작업 영역과 그 관계에 대해서 알아봤는데요. 이 부분은 몇 번을 강조해도 지나치지 않을만큼 중요한 핵심 개념입니다. 이 개념을 완벽히 
이해해야 나머지 내용을 배우는데 어려움이 없습니다. 꼭 제대로 이해하고 넘어가세요.

참고로 working directory는 working tree라고 하기도 하고, staging area는 index라고 할 때도 있습니다. 혹시 다른 곳에서 working tree, index 
이런 단어를 쓰더라도 결국 다 우리가 배운 작업 영역들이니까 당황하지 마세요!





=====================>
이전 노트에서 Git의 3가지 작업 영역을 배웠습니다. 
작업 영역과 관련해서 한 가지 더 알아두면 좋은 내용이 있는데요.
그건 바로 Git으로 관리되는 파일은 일종의 '상태(status)'라는 걸 가진다는 사실입니다. 
일단 Git에서 파일들은 크게 다음 2가지 상태를 가집니다.

Untracked 상태
Tracked 상태 
그리고 Tracked 상태는 다시 아래와 같은 3가지 상태로 나눌 수 있구요. 

Staged 상태
Unmodified 상태
Modified 상태
각 상태를 순서대로 설명해드릴게요.

1. Untracked 상태
Untracked는 '추적되지 않고 있는'이라는 뜻입니다. 이 상태는 파일이 Git에 의해서 그 변동사항이 전혀 추적되고 있지 않는 상태를 뜻합니다. 예를 들어, 
파일을 새로 생성하고 그 파일을 한 번도 git add 해주지 않았다면 이 상태입니다.

2. Tracked 상태
파일이 Git에 의해 그 변동사항이 추적되고 있는 상태입니다. 이 상태는 다시 그 특성에 따라 3가지 상태로 나뉩니다. 하나씩 설명할게요.

(1) Staged 상태
파일의 내용이 수정되고나서, staging area에 올라와있는 상태를 Staged(스테이징된, stage area에 올려진) 상태라고 합니다.
새로 생성한 파일에 내용을 쓰고 git add를 해주거나
한 번이라도 커밋에 포함됐었던 파일이라도 내용을 수정하고 git add를 해주면 이 상태입니다.

(2) Unmodified 상태
현재 파일의 내용이 최신 커밋의 모습과 비교했을 때 전혀 바뀐 게 없는 상태면 그 파일은 Unmodified(수정되지 않은, 변한 게 없는) 상태입니다. 
커밋을 하고 난 직후에는 working directory 안의 모든 파일들이 이 상태가 됩니다.

(3) Modified 상태
최신 커밋의 모습과 비교했을 때 조금이라도 바뀐 내용이 있는 상태면 그 파일은 Modified(수정된) 상태입니다.
이렇게 Git에서 파일은 매 순간 4가지 상태 중 하나의 상태에 있게 됩니다. 이 내용을 그림으로 정리하면 아래와 같습니다.          

====================>
이때까지 계속 git add, git commit처럼 git으로 시작하는 커맨드를 배우고 있죠? 앞으로도 계속 git으로 시작하는 커맨드들을 배울 겁니다. 

그런데 새롭게 커맨드를 배울 때마다 그 의미나 사용법을 좀더 자세히 알고 싶다면 어떻게 해야할까요?

그럴 때는 git help라는 커맨드를 쓰면 됩니다. 

git help [알고 싶은 커맨드의 이름]
의 형식으로 쓰면 되는데요. 예를 들어, git add라는 커맨드의 의미와 사용법을 좀더 자세히 알고 싶다고 해봅시다. 

또는

man git-[알고 싶은 커맨드]
형식으로 입력하고 실행해도 같은 결과가 출력됩니다. 그러니까 이렇게 입력해도


위와 같은 결과가 출력되는 겁니다. 

이렇게 출력되는 공식 메뉴얼에는 해당 git 커맨드에 대한 설명이 아주 자세하게 나와있습니다. 만약 이 공식 메뉴얼 화면에서 나가고 싶으면 영어 단어 quit(나가다)의 줄임말인 q를 입력하면 됩니다.

앞으로 커맨드를 새로 배울 때마다 더 자세하게 알고 싶은 게 있으면 위에서 배운대로 해보세요. 각각의 커맨드에 대해서 자세하게 알게 될수록 Git을 능숙하게 쓸 수 있게 될 겁니다. 모든 커맨드를 다 이렇게 자세히 알아보는 건 힘들겠지만 중요하거나 관심이 가는 커맨드는 이런 공식 메뉴얼을 활용해보세요.


-m 없이도 
git commit  메세지 남기기 