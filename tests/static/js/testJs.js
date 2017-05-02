"use strict"

function TestingMachine(qstnumfield, qstfield, answfields, inanswf, qstlistblock, qstblock) {

  var self = this;

  var activeQuestion = 0;
  var realQuestionList = [];
  var questions = {};
  var answerList = {};
  var questionsCount = 0;

  var activeQuestionField = qstnumfield;
  var questionField = qstfield;
  var answerFields = answfields;
  var inputAnswerFields = inanswf;
  var questionListBlock = qstlistblock;
  var questionsButtons = [];
  var questionBlock = qstblock;

  function timeoutErrorHandler() {

  };

  function requestErrorHandler() {

  };

  function choosingQuestionErrorHandler() {

  };

  function sendAnswers() {

  };

  function getQuestions() {
    var xmlRequest = new XMLHttpRequest();
    var body = 'qstCount' + encodeURIComponent('12'); // '12 кількісь питань'

    xmlRequest.open("POST", '/questions-generator', true);
    xmlRequest.setRequestHeader('Content-Type', 'application/x-www-urlencoded');
    xmlRequest.timeout = 10000;

    xmlRequest.send(body);

    xmlRequest.ontimeout = timeoutErrorHandler();
    xmlRequest.onerror = requestErrorHandler();
    xmlRequest.onload = function () {
      questions = JSON.parse(this.responseText);
      setQuestion(activeQuestion);
      generateQuestList();
      questionsButtons[activeQuestion].className += ' active';
    };
  };

  function setQuestion(questionNumber) {
    activeQuestionField.textContent = +questionNumber + 1;
    questionField.textContent = questions[questionNumber]['qst'];
    for (var answer = 0; answer < answerFields.length; answer++) {
      answerFields[answer].textContent = questions[questionNumber][answer];
    };

  }

  function generateQuestList() {
    var standart = document.createElement('button');
    var btn = 0;
    for (var i in questions) {
      questionsCount += 1;

      btn = standart.cloneNode(true);

      btn.className = 'choose-question';
      btn.textContent = +i + +1;
      btn.question = i;
      btn.onclick = chooseQuestion;

      questionsButtons.push(btn);

      questionListBlock.appendChild(btn);
    };


  };

  function chooseQuestion() {
    console.log("Choosed question: " + this.question);
    console.log(this.question);
    questionsButtons[activeQuestion].className = questionsButtons[activeQuestion].className.replace(' active', '');
    questionsButtons[+this.question].className += ' active';
    activeQuestion = +this.question;
    setQuestion(this.question);
    self.hideQuestionList();
  };

  // Обробник події відповіді
  this.reply = function () {
    // Змінна наступного питання, у ній зберігається номер наступного питання
    var nextQuestion = activeQuestion;
    var answered = false;

    // Запам'ятовуємо відповідь на данне питання у змінну answerList
    for (var i = 0; i < inputAnswerFields.length; i++) {
      if (inputAnswerFields[i].checked) {
        answerList[activeQuestion] = i;
        answered = true;
        break;
      };
    };

    if (!answered) { return 0; };

    // Робимо кнопку в виборі завдання "виконаною" і прибираємо з неї функцію вибору питання
    questionsButtons[activeQuestion].className = questionsButtons[activeQuestion].className.replace('active', 'answered');
    questionsButtons[activeQuestion].onclick = null;

    // Пробуємо знайти номер наступного не пройденого питання відштовхуючись від
    // номеру нинішнього питання аж до кінця
    while (questions[nextQuestion] && nextQuestion in answerList ) {
      nextQuestion++;
    };

    // Якщо ж ми дійшли до кінця всіх питань не знайшовши не пройденого питання,
    // то починаємо пошук з початку
    if (!questions[nextQuestion]) {
      nextQuestion = 0;
      while (questions[nextQuestion] && nextQuestion in answerList ) {
        nextQuestion++;
      };

    // Якщо обходячі усі питання ми так і не знайшли наступного питання, то вони всі пройдені, тест завершено.
      if (!questions[nextQuestion]) {
        console.log('Тест завершено');
        console.log(answerList);
        return 0;
       };


    };

    // Тепер активним питанням стає нове, знайдене питання
    activeQuestion = nextQuestion;

    // Виводимо нове питання
    setQuestion(nextQuestion);

    // Робимо кнопку наступного питання активною
    questionsButtons[nextQuestion].className += ' active';
  };

  this.pass = function () {
    var nextQuestion = activeQuestion + 1;

    // Пробуємо знайти номер наступного не пройденого питання відштовхуючись від
    // номеру нинішнього питання аж до кінця
    while (questions[nextQuestion] && nextQuestion in answerList ) {
      nextQuestion++;
    };

    // Якщо ж ми дійшли до кінця всіх питань не знайшовши не пройденого питання,
    // то починаємо пошук з початку
    if (!questions[nextQuestion]) {
      nextQuestion = 0;
      while (questions[nextQuestion] && nextQuestion in answerList ) {
        nextQuestion++;
      };
    };

    // Кнопка завдання яке ми пропускаємо перестає бути активною
    questionsButtons[activeQuestion].className = questionsButtons[activeQuestion].className.replace(' active', '');
    // Робимо кнопку наступного питання активною
    questionsButtons[nextQuestion].className += ' active';


    // Тепер активним питанням стає нове, знайдене питання
    activeQuestion = nextQuestion;

    // Виводимо нове питання
    setQuestion(nextQuestion);
  };

  // Показує меню вибору завдань (ніякої логіки, відповідає лише за показ цього меню)
  this.showQuestionList = function () {
    questionBlock.style.display = 'none';
    questionListBlock.style.display = 'block';
  };

  // Ховає меню вибору завдань (ніякої логіки, відповідає лише за ховання цього меню)
  this.hideQuestionList = function () {
    questionListBlock.style.display = 'none';
    questionBlock.style.display = 'block';
  }

  getQuestions();

};



var qf = document.querySelector('.exercise p');
var af = document.querySelectorAll('.input-block label');
var inanswf = document.querySelectorAll('.input-block input');
var qnf = document.querySelector('.question-number');
var nextButton = document.querySelector('.answ-btn');
var passButton = document.querySelector('.pass-btn');
var qstlistblock = document.querySelector('#question-list');
var questionBlock = document.querySelector('#question');
var listButton = document.querySelectorAll('.list-btn');

var tester = new TestingMachine(qnf, qf, af, inanswf, qstlistblock, questionBlock);
nextButton.onclick = tester.reply;
passButton.onclick = tester.pass;
listButton[0].onclick = tester.showQuestionList;
listButton[1].onclick = tester.hideQuestionList;
