package com.yn.likelion.crud.post;

public class PostDto {//Data Transfer Objet : 데이터를 주고받는데 사용되는 개체, 테이블 일관성을 위한 완충재 역할
    private String title;
    private String content;
    private String writer;

    public PostDto(){}
    public PostDto(String title, String content, String writer){
        this.title = title;
        this.content = content;
        this.writer = writer;
    }

    public String getTitle(){
        return title;
    }

    public void setTitle(String title){
        this.title = title;
    }

    public String getContent(){
        return content;
    }

    public void setContent(String content){
        this.content = content;
    }

    public  String getWriter(){
        return writer;
    }

    public void setWriter(String writer){
        this.writer = writer;
    }

    @Override
    public String toString(){
        return "PostDto{" + "title=" + title + "\\"+
                ", content=" + content + "\\"+
                        ", writer=" + writer + "\\"+ "}";
    }
}
