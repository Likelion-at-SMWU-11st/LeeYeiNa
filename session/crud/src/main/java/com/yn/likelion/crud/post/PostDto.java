package com.yn.likelion.crud.post;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class PostDto {//Data Transfer Objet : 데이터를 주고받는데 사용되는 개체, 테이블 일관성을 위한 완충재 역할
    private int id;
    private String title;
    private String content;
    private String writer;
    private int baordId;

    public PostDto(int id, String title, String content, String writer, int boardId){
        this.id = id;
        this.title = title;
        this.content = content;
        this.writer = writer;
        this.baordId = boardId;
    }

//    public String getTitle(){
//        return title;
//    }
//
//    public void setTitle(String title){
//        this.title = title;
//    }
//
//    public String getContent(){
//        return content;
//    }
//
//    public void setContent(String content){
//        this.content = content;
//    }
//
//    public  String getWriter(){
//        return writer;
//    }
//
//    public void setWriter(String writer){
//        this.writer = writer;
//    }
//
//    @Override
//    public String toString(){
//        return "PostDto{" + "title=" + title + "\\"+
//                ", content=" + content + "\\"+
//                        ", writer=" + writer + "\\"+ "}";
//    }
}
