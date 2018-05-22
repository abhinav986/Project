import { Component, OnInit, Input } from '@angular/core';
import { InstructorServiceService } from '../../instructor-service/instructor-service.service';
import { ToastService } from '../../../typescripts/pro';

@Component({
  selector: 'app-quiz',
  templateUrl: './quiz.component.html',
  styleUrls: ['./quiz.component.scss']
})
export class QuizComponent implements OnInit {

  id: string;
  options: { closeButton: boolean; tapToDismiss: boolean; positionClass: string; };
  quizData: any = {};
  correctAnswer = '';
  correctAnswer1 = false;
  correctAnswer2 = false;
  correctAnswer3 = false;
  correctAnswer4 = false;
  status: boolean = true;
  private _quizId: any;
  private _quizOrderNumber: number;
  @Input()

  set quizId(quizId: any) {
    this._quizId = (quizId) || [];
  }

  get quizId(): any {
    return this._quizId;
  }

  @Input()
  set quizOrderNumber(quizOrderNumber: number) {
    this._quizOrderNumber = (quizOrderNumber);
  }

  constructor(private instructorService: InstructorServiceService, private toastService: ToastService) { }

  ngOnInit() {
    this.options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
    this.id = 'quiz' + this._quizId;
  }

  sumitQuiz(quiz_Id) {
    const type_id = 1; // default value
    if (this.correctAnswer1 == false && this.correctAnswer2 == false && this.correctAnswer3 == false && this.correctAnswer4 == false) {
      this.toastService.info('', 'Please select a correct answer..!', this.options);
    } else {
      const answer = [
        {
          option: this.quizData.option1,
          answer: this.correctAnswer1
        },
        {
          option: this.quizData.option2,
          answer: this.correctAnswer2
        },
        {
          option: this.quizData.option3,
          answer: this.correctAnswer3
        },
        {
          option: this.quizData.option4,
          answer: this.correctAnswer4
        }
      ]
      this.instructorService.addQuizQuestion(quiz_Id, this._quizOrderNumber, this.quizData, this.status, type_id, JSON.stringify(answer)).subscribe(data => {
        if (data['status'] === 1) {
          this.toastService.success('', data['msg'], this.options);
        } else {
          this.toastService.error('', data['error'], this.options);
        }
      });
    }
  }
} 