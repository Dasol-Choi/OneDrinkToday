const qna = document.querySelector('#qna')
const main = document.querySelector('#main')
const result = document.querySelector('#result')

/*****
 * 데이터 생성
 ******/
const questions = [`
        <p id="question" class="question">1) 어떤 맛을 좋아하나요?</p>
        <div id="buttons" class="buttons">
            <button class="btn-a btn-outline-primary" value="1">달달함</button>
            <button class="btn-a btn-outline-primary" value="2">상큼함</button>
            <button class="btn-a btn-outline-primary" value="3">드라이함</button>
        </div>
    `,
    `
        <p id="question" class="question">2) 어떤 도수를 좋아하나요?</p>
        <div id="buttons" class="buttons">
            <button class="btn-a btn-outline-primary" value="1">높은 도수</button>
            <button class="btn-a btn-outline-primary" value="2">낮은 도수</button>
        </div>
    `,
    `
        <p id="question" class="question">3) 어떤 이미지를 좋아하나요?</p>
        <div id="buttons" class="buttons">
            <button class="btn-a btn-outline-primary" value="1">화려함</button>
            <button class="btn-a btn-outline-primary" value="2">심플함</button>
        </div>
    `,
    `
        <p id="question" class="question">4) 누구와 함께 마시나요?</p>
        <div id="buttons" class="buttons">
            <button class="btn-a btn-outline-primary" value="1">혼자</button>
            <button class="btn-a btn-outline-primary" value="2">연인과 함께</button>
            <button class="btn-a btn-outline-primary" value="3">친구와 함께</button>
        </div>    `
]

// 퀴즈 정보 객체
function Quiz(questions) {
   this.selectAnswer = '';
   this.questions = questions; // 문제
   this.questionIndex = 0; // 문제 번호
}

// 퀴즈 객체 생성
const quiz = new Quiz(questions);

/*****
 * ui event
 ******/
// 상태 진행바
 function status() {
    const status = document.querySelector('.statusBar');
    status.style.width = (100 /quiz.questions.length) * (quiz.questionIndex + 1 ) + '%'
}

// 팝업 첫화면 > 시작하기 클릭
function begin(){
    main.style.display = "none";
    qna.style.display = "block";
    updateQuiz();
}

function updateQuiz() {
    let quizEl = document.querySelector('#qna #quiz');
    quizEl.innerHTML = quiz.questions[quiz.questionIndex];
    addEvent();
    status();
}

// 팝업 퀴즈 > 답변에 click이벤트 부여
function addEvent(){
    let btnCnt = document.querySelectorAll('#qna .btn-a');
    for (let i = 0; i < btnCnt.length; i++) {
       checkAnswer(btnCnt[i]);
    }
}

// 답변 클릭시 실행되는 함수
function checkAnswer(btn) {
   btn.addEventListener('click', function() {
      let answer = btn.value;
      quiz.selectAnswer += answer; // 선택한 답 밀어 넣기

      // 문제 끝날 때까지 문제 출력
      if (quiz.questionIndex < quiz.questions.length - 1) {
         quiz.questionIndex++;
         updateQuiz();
      } else {
         goResult();
      }
   });
}

// 결과
function findResult(element) {
    if (element.index === quiz.selectAnswer) {
        return true;
    }
}

function goResult() {
    qna.style.display = "none";
    result.style.display = "block";
    const fr = resultList.find(findResult);
    $('.resultName_k').append(fr.name_k)
    $('.resultName_e').append(fr.name_e)
    const img = fr.img;
    const temp_html = `<img class="img-box" src="${img}">`
    $('.resultImg').append(temp_html)
}

// 팝업 마지막 > 다시테스트 하기 클릭
function goToMain(){
    // 문제 초기화
    quiz.selectAnswer = '';
    quiz.questionIndex = 0;
    $( '.resultName_k' ).empty()
    $( '.resultName_e' ).empty()
    $( '.resultImg' ).empty()

    // 결과화면에서 시작화면으로 변경
    result.style.display ="none";
    qna.style.display ="none";
    main.style.display ="block";
}

//칵테일 정보 페이지 이동
 function goToDesc() {
    const fr = resultList.find(findResult);
    const cocktailName = fr.name_e
    const url =  `/`+ cocktailName;
    window.location.href=url;
    }


 $('#modal').on('hidden.bs.modal', function e(){
      // 문제 초기화
    quiz.selectAnswer='';
    quiz.questionIndex=0;
    $( '.resultName_k' ).empty()
    $( '.resultName_e' ).empty()
    $( '.resultImg' ).empty()

    // 결과화면에서 시작화면으로 변경
    result.style.display ="none";
    qna.style.display ="none";
    main.style.display ="block";
 });

//카카오톡 연결하기
function kakaoShare() {
    const fr = resultList.find(findResult);
    const cocktailName = fr.name_e;
    const img = fr.img;

    Kakao.Link.sendDefault({
        objectType: 'feed',
        content: {
            title: '오늘의 한 잔은?',
            description: cocktailName,
            imageUrl: img,
            link: {
                webUrl : `http://오늘한잔.shop/`+cocktailName,
                mobileWebUrl : `http://오늘한잔.shop/`+cocktailName,
                androidExecutionParams: 'test',
                iosExecutionParams: 'test'
            },
        },

        buttons: [
            {   title: '웹으로 이동',
                link: {
                    webUrl: `http://오늘한잔.shop/`+cocktailName,
                    mobileWebUrl : `http://오늘한잔.shop/`+cocktailName,
                    androidExecutionParams: 'test',
                    iosExecutionParams: 'test'
                },
            }
        ]
    });
}