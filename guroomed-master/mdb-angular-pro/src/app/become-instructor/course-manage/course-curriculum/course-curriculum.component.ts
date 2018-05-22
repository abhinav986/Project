import { Component, OnInit } from '@angular/core';
import { InstructorServiceService } from '../../instructor-service/instructor-service.service';
import { ActivatedRoute } from '@angular/router';
import { ToastService } from '../../../typescripts/pro';

@Component({
  selector: 'app-course-curriculum',
  templateUrl: './course-curriculum.component.html',
  styleUrls: ['./course-curriculum.component.scss']
})
export class CourseCurriculumComponent implements OnInit {
  quizOrderNo: number;
  options: { closeButton: boolean; tapToDismiss: boolean; positionClass: string; };
  progress_bar: boolean;
  videoFileToUpload: File;
  course_id: any;
  addLecture: any = {};
  sectionAdded: any = {};
  newSectionAdded = [];
  addedNewLecture = [];
  sectionOrderNo = 0;
  lectureOrderNo = 0;
  addQuiz: any = {};
  addQuizQuestion;
  constructor(private instructorService: InstructorServiceService, private route: ActivatedRoute, private toastService: ToastService) { }

  ngOnInit() {
    this.course_id = this.route.snapshot.parent.params.id;
    this.getCurriculumData(this.course_id);

    this.options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
  }

  // Get All Curriculum
  getCurriculumData(course_id) {
    this.instructorService.getCurriculum(course_id).subscribe(getData => {
      if (getData['status'] === 1) {
        this.newSectionAdded = getData['curriculum'];
        this.sectionOrderNo = this.newSectionAdded.length;
        this.newSectionAdded.forEach(element => {
          this.lectureOrderNo = element.curriculumLect.length
          this.quizOrderNo = element.curriculumQuiz.length
        });
      }
    });
  }

  // Add quiz question
  addQuestion(){
    this.addQuizQuestion = true;
  }


  // Add New Section
  sectionAdd() {
    if (this.sectionAdded.section_name === undefined) {
      this.toastService.error('', 'Please enter section name', this.options);
    } else {
      this.instructorService.addCurriculum(this.course_id, this.sectionAdded, this.sectionOrderNo + 1).subscribe(data => {
        if (data['status'] === 1) {
          this.getCurriculumData(this.course_id);
        }
      });
    }
  }

  // Upload lecture video file
  videoUpload(videoFile: FileList) {
    this.videoFileToUpload = videoFile.item(0);
    if (this.videoFileToUpload) {
      const videoFileReader = new FileReader();
      videoFileReader.readAsDataURL(this.videoFileToUpload)
    }
  }

  // Add Quiz
  saveQuiz(section_id) {
    if (this.addQuiz.quiz_title === undefined || this.addQuiz.quiz_description === undefined) {
      this.toastService.error('', 'Please add quiz data', this.options);
    } else {
      this.instructorService.addCurriculumQuiz(section_id, this.addQuiz).subscribe(data => {
        if (data['status'] === 1) {
          this.toastService.success('', data['msg'], this.options);
          this.getCurriculumData(this.course_id);
        } else {
          this.toastService.error('', 'Something went wrong', this.options);
        }
      });
    }
  }

  // Save curriculum
  saveLecture(section_id) {
    if (this.addLecture.lecture_name === undefined || this.videoFileToUpload === undefined) {
      this.toastService.error('', 'Please add lecture data', this.options);
    } else {
      this.progress_bar = true;
      this.instructorService.addCurriculumLectures(section_id, this.addLecture, this.lectureOrderNo + 1, this.videoFileToUpload).subscribe(data => {
        this.progress_bar = false;
        if (data['status'] == 1) {
          this.toastService.success('', data['msg'], this.options);
          this.getCurriculumData(this.course_id);
        } else {
          this.toastService.error('', 'Something went wrong', this.options);
        }
      });
    }
  }
}