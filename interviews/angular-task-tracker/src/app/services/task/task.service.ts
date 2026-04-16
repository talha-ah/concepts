import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Task } from './task';

const API = 'http://localhost:5000/tasks';

const options = {
  headers: new HttpHeaders().set('Content-Type', 'application/json'),
};

@Injectable({
  providedIn: 'root',
})
export class TaskService {
  tasks: Task[] = [];

  constructor(private http: HttpClient) {}

  getTasks(): Observable<Task[]> {
    return this.http.get<Task[]>(API);
  }

  addTask(task: Task) {
    return this.http.post<Task>(API, task, options);
  }

  deleteTask(task: Task) {
    return this.http.delete<Task>(`${API}/${task.id}`, options);
  }

  toggleTaskReminder(task: Task) {
    return this.http.put<Task>(`${API}/${task.id}`, task, options);
  }
}
