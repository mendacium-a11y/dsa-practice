#include <iostream>
#include <queue>
using namespace std;

class node
{
public:
    int data;
    node *left;
    node *right;

    node(int data)
    {
        this->data = data;
        this->left = nullptr;
        this->right = nullptr;
    }
};

void BSTcreate(node *&root, int data)
{
    if (root == NULL)
    {
        root = new node(data);
        return;
    }

    if (data > root->data)
    {
        BSTcreate(root->right, data);
    }

    if (data < root->data)
    {
        BSTcreate(root->left, data);
    }
}

void level(node *root)
{
    queue<node *> q;
    q.push(root);
    q.push(NULL);

    while (!q.empty())
    {
        node *temp = q.front();
        q.pop();

        if (temp == NULL)
        {
            cout << endl;

            if (!q.empty())
            {
                q.push(NULL);
            }
        }
        else
        {
            cout << temp->data;

            if (temp->left)
            {
                q.push(temp->left);
            }
            if (temp->right)
            {
                q.push(temp->right);
            }
        }
    }
}

void largestNode(node *root)
{
    while (root->right != nullptr)
    {
        root = root->right;
    }
    cout << root->data << endl
         << endl
         << endl;
}

void smallestNode(node *root)
{
    while (root->left != nullptr)
    {
        root = root->left;
    }
    cout << root->data << endl
         << endl
         << endl;
}

int findBST(node *root, int data)
{

    while (root)
    {
        if (data > root->data)
        {
            root = root->right;
        }
        if (data < root->data)
        {
            root = root->left;
        }
        if (data == root->data)
        {
            cout << root << endl
                 << endl
                 << endl;
            return 1;
        }
    }
    return -1;
}

int main()
{
    // node* tree = new node(1);
    // tree->left = new node(2);
    // tree->right = new node(3);
    // tree->left->left = new node(4);
    // tree->left->right = new node(5);
    // tree->right->left = new node(6);
    // tree->right->right = new node(7);

    // // node* tree = new node(1);
    // // buildLevel(tree);
    // level(tree);

    // // irt(tree);
    // pprt(tree);
    node *tree = new node(5);
    BSTcreate(tree, 10);
    BSTcreate(tree, 2);
    BSTcreate(tree, 12);
    BSTcreate(tree, 4);
    BSTcreate(tree, 7);

    // level(tree);
    // largestNode(tree);
    // smallestNode(tree);
    findBST(tree, 10);

    return 1;
}