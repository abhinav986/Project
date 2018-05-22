import { Component, OnInit } from '@angular/core';
import { InstructorServiceService } from '../../instructor-service/instructor-service.service';
import { ActivatedRoute } from '@angular/router';
import { ToastService } from '../../../typescripts/pro';

@Component({
  selector: 'app-course-goals',
  templateUrl: './course-goals.component.html',
  styleUrls: ['./course-goals.component.scss']
})
export class CourseGoalsComponent implements OnInit {
  knowledgeRequired: any = [{ value: '' }];
  targetStudent: any = [{ value: '' }];
  learnGoal: any = [{ value: '' }];
  course_id: number;
  constructor(private instructorService: InstructorServiceService, private toastrService: ToastService, private route: ActivatedRoute) { }

  ngOnInit() {
    this.course_id = this.route.snapshot.parent.params.id;
    this.getList(this.course_id);
  }

  getList(course_id) {
    this.instructorService.getList(course_id).subscribe(data => {
      this.knowledgeRequired[0].value = data['draft'].knowledgeRequired;
      this.targetStudent[0].value = data['draft'].targetStudent;
      this.learnGoal[0].value = data['draft'].what_will_i_learn;
    });
  }

  addKnowledgeRequired() {
    this.knowledgeRequired.push({ value: '' });
  }
  removeKnowledgeRequired(i) {
    this.knowledgeRequired.splice(i, 1);
  }

  addTargetStudent() {
    this.targetStudent.push({ value: '' });
  }
  removeTargetStudent(i) {
    this.targetStudent.splice(i, 1);
  }

  addLearnGoal() {
    this.learnGoal.push({ value: '' });
  }
  removeLearnGoal(i) {
    this.learnGoal.splice(i, 1);
  }

  onCourseGoalsSubmit() {
    // const courseGoal = {
    //   knowledgeRequired: this.knowledgeRequired,
    //   targetStudent: this.targetStudent,
    //   learnGoal: this.learnGoal
    // }
    if (this.knowledgeRequired[0].value != '' || this.targetStudent[0].value != '' || this.learnGoal[0].value != '') {

      let options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
      this.instructorService.saveCourseGoals(this.course_id, this.knowledgeRequired[0].value, this.targetStudent[0].value, this.learnGoal[0].value).subscribe(data => {
        if (data['status'] == 1) {
          this.getList(this.course_id);
          this.toastrService.success('', 'Course goals saved successfully as a draft', options);
        } else {
          this.toastrService.error('', 'Something went wrong..! ', options);
        }
      });
    }
  }

}
