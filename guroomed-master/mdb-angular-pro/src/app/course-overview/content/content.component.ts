import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { InstructorServiceService } from '../../become-instructor/instructor-service/instructor-service.service';
import { LoaderService } from '../../shared/loader/loader.service';

@Component({
  selector: 'app-content',
  templateUrl: './content.component.html',
  styleUrls: ['./content.component.scss']
})
export class ContentComponent implements OnInit {
  lectureOrderNo: any;
  sectionOrderNo: any;
  sectionData: any;
  draftReference: string;
  course_id: number;

  constructor(private route: ActivatedRoute, private router: Router, private instructorService: InstructorServiceService, private loader: LoaderService,) { }

  ngOnInit() {
    this.loader.show();
    this.course_id = this.route.snapshot.parent.params.id;
    this.draftReference = this.route.snapshot['_routerState'].url.split('/')[3];
    if(this.draftReference == 'draft-content'){
      this.getCurriculumData(this.course_id);
    }
   
  }

  getCurriculumData(course_id) {
    this.instructorService.getCurriculum(course_id).subscribe(getData => {
      if (getData['status'] == 1) {
        this.loader.hide();
        this.sectionData = getData['curriculum'].reverse();
        this.sectionOrderNo = this.sectionData.length;
        this.sectionData.forEach(element => {
          this.lectureOrderNo = element.curriculumLect.length;
        });
      }
    });
  }

  onLecturesClick(course_id, lecData){
    this.router.navigate(['instructor' , 'course', 'draft-content', 'lecture', { id: course_id, video_id: lecData.video_url }]);
  }

  onQuizClick(course_id, quizData) {
    this.router.navigate(['instructor', 'course', 'draft-content', 'quiz', { id: course_id, quiz_id: quizData.id}])
  }

}
