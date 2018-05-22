import { Component, OnInit } from '@angular/core';
import { NavbarService } from 'app/shared/navbarService/navbar.service';
import { Router, ActivatedRoute } from '@angular/router';
import { InstructorServiceService } from '../../become-instructor/instructor-service/instructor-service.service';

@Component({
  selector: 'app-lectures',
  templateUrl: './lectures.component.html',
  styleUrls: ['./lectures.component.scss']
})
export class LecturesComponent implements OnInit {
  showResponse: boolean;
  success: string;
  answerResponse: string;
  answer: any;
  is_correct = [];
  isQuizActive: boolean;
  sectionData: any;
  quiz_Id: any;
  currentUrl: string;
  course_id: any;
  id: number;
  video_Id: string;
  url: any;
  marginLeft: number;
  width: number;
  transition: string;
  sideNavOpened: boolean = false;
  itemsList;

  constructor(public nav: NavbarService, private router: Router, private route: ActivatedRoute, private instructorService: InstructorServiceService) { }

  ngOnInit() {
    this.nav.hide();
    this.currentUrl = this.route.snapshot.routeConfig.path.split('/')[2];
    this.route.params.subscribe(params => {
      this.course_id = params.id;
      this.quiz_Id = params['quiz_id'];
      this.video_Id = params['video_id'];
      this.video_Id = `https://player.vimeo.com/video/${this.video_Id}`;
      if (this.quiz_Id) {
        this.quizData(this.quiz_Id, this.course_id);
      }
    });
  }

  quizData(quiz_id, course_id) {
    this.quiz_Id = quiz_id;
    this.instructorService.getCurriculum(course_id).subscribe(getData => {
      if (getData['status'] == 1) {
        this.sectionData = getData['curriculum'].reverse();
        this.sectionData.forEach(element => {
          (element.curriculumQuiz).forEach(element => {
            if (this.quiz_Id == element.id) {
              (element.quizQuestion).forEach(element => {
                (element.answer).forEach(element => {
                  if (element.is_correct) {
                    this.is_correct = element.is_correct;
                  }
                })
              });
            }
          });
        });
      }
    });
  }

  openNav() {
    this.sideNavOpened = true;
    document.getElementById("mySidenav").style.width = "500px";
    document.getElementById("main").style.marginLeft = "500px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  }

  closeNav() {
    this.sideNavOpened = false;
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = "white";
  }

  gotoDashboard() {
    if (this.currentUrl == 'draft-content') {
      this.router.navigate(['/instructor', 'course', 'draft-content', this.course_id, 'content']);
    } else {
      this.router.navigate(['/mycourses']);
    }
  }

  startQuiz() {
    this.isQuizActive = true;
  }

  isSelected(ans) {
    this.answer = ans;
  }

  checkAnswer() {
    this.showResponse = true;
    if (this.answer == undefined) {
      this.success = 'danger';
      this.answerResponse = 'Please select your option to check';
    } else if (this.answer == this.is_correct) {
      this.success = 'success';
      this.answerResponse = 'Correct Answer';
    } else {
      this.success = 'danger';
      this.answerResponse = 'Wrong Answer';
    }
  }

  hideResponse() {
    this.showResponse = false;
  }

}
